# **Snotify** version 0.1.0 (02-2019)

**Snotify** is a simple notification tool for Spotifyd written in Python 3.7.

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

`pip uninstall snotify

rm -rf ~/.config/snotify`

Remove the **onevent** line in your spotifyd.conf file and restart Spotifyd.

