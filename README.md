# **Snotify** version 0.3.0 (03-2019)

**Snotify** is a simple notification tool and a basic playback controller for Spotifyd written in Python 3.7.

*Dependencies: spotipy, spotify-token, dunst (or similar)*

## 1. Installation

First, clone this repository then install Snotify:

`python setup.py install --user`

## 2. Configuration

Add this line to your Spotifyd config file (~/.config/spotifyd/spotifyd.conf):

`onevent = /home/username/.local/bin/snotify`

Then launch snotify. It will prompt you for your Spotify username and password.

*Note: A configuration file named config will be stored in ~/.config/snotify/*

Finally restart Spotifyd:

`systemctl --user restart spotifyd.service`

That's it. A notification should display on song start / change / stop.

## 3. Usage

*Note: It is possible to use Snotify from the command line.*

### 3.1 Notification format

You can specify what to display by using the -f (--format) option. For instance :

`snotify -f '%n: %t'`

displays artist and trackname.


Possible variables are:

- %n artist name
- %t track title
- %a album
- %y year of release
- %d track duration
- %p track progress
- %s playback state

By default, Snotify displays "artist: track title". That said, if you want to change notification format, you have to use the included **snotifier** script (copy it somewhere and modify it) and change the **onevent** option in the Spotifyd configuration file accordingly.

`onevent = /home/username/bin/snotifier`

If you want to preview a notification for a particular format, you can use the -n (--notify) option from the command line.

`snotify --notify --format '%n: %t'`

### 3.2 Playback control

Snotify also provides basic playback control with the -a option.

- toggle
- play
- pause
- next
- prev

### 3.3 Command line options

-h --help

-f --format=FORMAT text format

-n --notify - display notification

-F --force - force output to stdout

-a toggle,play,pause,next,prev - playback control

-v --version

## 4. Uninstall

`pip uninstall snotify`

`rm -rf ~/.config/snotify`

Remove the **onevent** line in your spotifyd.conf file and restart Spotifyd.
