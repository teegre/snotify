import spotipy
from getpass import getpass
import spotify_token as st
from time import time
import os
import sys
import subprocess
import pprint

config_dir = os.getenv('HOME') + '/.config/snotify'
config_file = config_dir + '/config'
output_file = config_dir + '/output'

def xinput(prompt, pwd=False):
    if pwd: return getpass(f'{prompt}: ')
    else: return input(f'{prompt}: ')

def get_auth():
    # Read / Write configuration file.
    try:
        with open(config_file, 'r') as f:
            config = f.read()
            return config.split('\n')
    except FileNotFoundError:
        if not os.path.exists(config_dir):
            os.makedirs(config_dir)
        username = xinput('username')
        password = xinput('password', pwd=True)
        with open(config_file, 'w') as f:
            f.write('/n'.join([username, password, '', '']))
        os.chmod(config_file, 0o600)
        return [username, password, '', '']

def get_token():
    config = get_auth()
    token = config[2]
    expiracy_date = int(config[3])
    if not token or (expiracy_date - time() <= 0):
        data = st.start_session(username=config[0], password=config[1])
        if data:
            config[2] = data[0]
            config[3] = str(data[1])
            with open(config_file, 'w') as f:
                f.write('\n'.join(config))
            token = config[2]
            del config
            return token
        else:
            del config
            return None
    else:
        del config
        return token

class Track():
    def __init__(self, track):
        self.__track__ = track
        self.artists = []
        self.name = ''
        self.album = ''
        self.year = ''
        self.parse()
    def parse(self):
        self.name = self.__track__['name']
        self.artists = '/'.join([artist['name'] for artist in self.__track__['album']['artists']])
        self.album = self.__track__['album']['name']
        self.year = self.__track__['album']['release_date'][:4]

def main():
    event = os.getenv('PLAYER_EVENT')
    trackid = os.getenv('TRACK_ID')
    token = get_token()
    if not token:
        print('err: something went wrong...')
        sys.exit(33)
    if event == 'start' or event == 'change':
        urn = f'spotify:track:{trackid}'
        sp = spotipy.Spotify(auth=token)
        track = Track(sp.track(urn))
        output = f'<b>{track.name}</b>\n{track.artists}\n<i>{track.album}</i>\n{track.year}'
        subprocess.Popen(['notify-send', '-a', 'Spotifyd', '-t', '5000', '-u', 'low', output])
    else:
        subprocess.Popen(['notify-send', '-a', 'Spotifyd', '-t', '5000', '-u', 'low', 'Stopped'])
