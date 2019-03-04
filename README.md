# **Snotify** version 0.3.0 (03-2019)

**Snotify** is a simple notification tool and playback controller for Spotifyd written in Python 3.7.

> Dependencies:

> spotipy, spotify-token, dunst (or similar)

## 1. Installation

First, clone this repository then install Snotify:

`python setup.py install --user`

## 2. Configuration

Add this line to your Spotifyd config file (~/.config/spotifyd/spotifyd.conf):

`onevent = /home/username/.local/bin/snotify`

Then launch snotify. It will prompt you for your Spotify username and password.

> Note: A configuration file named config will be stored in ~/.config/snotify/)

Finally restart Spotifyd:
`systemctl --user restart spotifyd.service`

That's it. A notification should display on song start / change / stop.

## 3. Uninstall

`pip uninstall snotify`

`rm -rf ~/.config/snotify`

Remove the **onevent** line in your spotifyd.conf file and restart Spotifyd.

## 4. Usage

Snotify [-h] [-a {play,pause,next,previous}] [-f <format>] [--loop]
               [-v]

Notification tool and simple playback controller for Spotifyd.

optional arguments:
  -h, --help            show this help message and exit
  -a {play,pause,next,previous}
                        playback control.
  -f <format>, --format <format>
  --loop                continuous display
  -v, --version         show program's version number and exit

Formatting: %t track title, %n artist name,%a album name, %y year of release,
%d track duration, %p elapsed time
