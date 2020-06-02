from os import getenv, makedirs, chmod
from subprocess import Popen
from time import time
from urllib.request import urlopen
import argparse
import base64
from . import config
import os.path
import requests
import sys

__version__ = '1.0'

def err(message):
    term = getenv('TERM')
    if term != 'linux': print(f'snotify: {message}')
    else: Popen(['notify-send', '-u', 'critical', 'snotify', message])


def notify(message, album_art=None, duration=5000):
    if album_art:
        Popen(['notify-send', '-t', str(duration), '-u', 'low', '-i', album_art, message])
    else:
        Popen(['notify-send', '-t', str(duration), '-u', 'low', message])


class Track():
    def __init__(self, trackid, token):
        self.__id = trackid
        self.__token = token
        self.artists = ''
        self.title = ''
        self.album = ''
        self.year = ''
        self.album_art = ''
        self.__cachedir = getenv('HOME') + '/.config/snotify/cache'
        if not os.path.exists(self.__cachedir):
            makedirs(self.__cachedir)
        self.__get_track_info()

    def __get_track_info(self):
        # requesting track info

        if not self.__token: return False

        headers = {'Authorization': f'Bearer {self.__token}'}
        r = requests.get(
            f'https://api.spotify.com/v1/tracks/{self.__id}',
            headers=headers
        )

        try:
            r.raise_for_status()
            tr = r.json()
            self.title = tr['name']
            self.artists = '/'.join(artist['name'] for artist in tr['artists'])
            self.album = tr['album']['name']
            self.year = tr['album']['release_date'][:4]

            image_url = tr['album']['images'][2]['url']
            filename = image_url.split('/')[-1] + '.jpg'
            self.album_art = self.__get_album_art(image_url, filename)
            return True
        except requests.HTTPError as e:
            err(f'{str(e).lower()}')
            return False
        except KeyError:
            err(f'unable to get track info!\nreason: {r.json()["error_description"].lower()}')
            return False

    def __get_album_art(self, url, filename):
        # download album art if not already in cache
        filepath = f'{self.__cachedir}/{filename}'
        if os.path.exists(filepath): return filepath
        else:
            try:
                with urlopen(url) as r, open(filepath, 'wb') as output:
                    data = r.read()
                    output.write(data)
                    return filepath
            except Exception as e:
                err(f'unable to get album_art\nreason: {str(e).lower()}')
                return ''

class Token():
    """
    Token class
    return an access token
    """
    def __init__(self):
        self.__config_dir = getenv('HOME') + '/.config/snotify'
        self.__token_file = self.__config_dir + '/token'
        self.__token = ''
        self.__expiration_date = 0
        self.__get_auth()

    def __get_token(self):
        # get access token from Spotify®

        creds = f'{config.cid}:{config.cs}'
        encoded_creds = base64.b64encode(creds.encode()).decode()

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': f'Basic {encoded_creds}'
        }

        params = {'grant_type': 'client_credentials'}

        r = requests.post(
            'https://accounts.spotify.com/api/token',
            headers=headers,
            params=params
        )

        try:
            self.__token = r.json()['access_token']
            self.__expiration_date = int(r.json()['expires_in']) + int(time())
            return True
        except KeyError:
            err(f'unable to obtain access token!\nreason: {r.json()["error_description"].lower()}')
            self.__token = ''
            self.__expiration_date = 0
            return False

    def __check_token(self):
        if not self.isvalid:
            self.__get_token()
            if self.__token: self.__save_token()
            else: return False
        return True

    def __save_token(self):
        with open(self.__token_file, 'w') as f:
            f.write(f'{self.__token}:{self.__expiration_date}')

    def __get_auth(self):
        # get access token from token file
        # if no token file is found, create a new one
        # and get a new access token from Spotify®
        try:
            with open(self.__token_file, 'r') as f:
                t, d = f.read().split(':')
                self.__token = t
                self.__expiration_date = int(d)
                self.__check_token()
        except FileNotFoundError:
            if not os.path.exists(self.__config_dir):
                makedirs(self.__config_dir)
            if self.__get_token():
                self.__save_token()
                chmod(self.__token_file, 0o600)
                return True
            else:
                return False

    def __repr__(self):
        return self.value

    @property
    def isvalid(self):
        if self.__expiration_date - int(time()) <= 0:
            return False
        else: return True

    @property
    def value(self):
        if not self.isvalid:
            self.__get_auth()
        return self.__token

def get_info(trackid, token, _format=None):
    # return a tuple containing given track info (_format)
    # and album art
    if not token: return None, None
    track = Track(trackid, token)
    if not track: return None, None
    if _format:
        # expand variables
        _format = _format.replace('%title', track.title)
        _format = _format.replace('%artist', track.artists)
        _format = _format.replace('%album', track.album)
        _format = _format.replace('%year', track.year)
        return _format, track.album_art
    else:
        output = f'{track.artists}: {track.title}'
        return output, track.album_art

def shell(_format=None, image=False, force=False):
    token = Token()
    if not token.value:
        err('something went wrong...')
        sys.exit(1)
    event = getenv('PLAYER_EVENT')
    trackid = getenv('TRACK_ID')
    if (event == 'start' or event == 'change'):
        track, album_art = get_info(trackid, token, _format)
        if track:
            if not force:
                if image: notify(track, album_art)
                else: notify(track)
            else: print(track)
    elif event == 'stop' and not force: notify("stopped")

def parse_args():
    p = argparse.ArgumentParser(
        prog='snotify',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='Simple Notification tool for Spotifyd',
        epilog="""
notification format:
%title  -- track title
%artist -- artist name
%album  -- album title
%year   -- year of release"""
    )
    p.add_argument('-f', '--format', metavar='<format>', type=str, default=None)
    p.add_argument('-i', '--image', action='store_true', help='display album art')
    p.add_argument('-F', '--force', action='store_true', help='force output to stdout')
    p.add_argument('-v', '--version', action='version', version=f'Snotify version {__version__}')
    args = p.parse_args()
    shell(args.format, args.image, args.force)

def main():
    parse_args()
