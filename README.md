# **Snotify** version 0.4.0 (12-2019)

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

`snotify -f '%artist: %title'`

displays artist and trackname.


Possible variables are:

|Variable |Description
|:--------|:----------
|%artist |artist name
|%title |track title
|%album |album
|%date |year of release
|%duration |track duration
|%progress |track progress
|%status |playback state

By default, Snotify displays "artist: track title". That said, if you want to change notification format, you have to use the included **snotifier** script (copy it somewhere and modify it) and change the **onevent** option in the Spotifyd configuration file accordingly.

`onevent = /home/username/bin/snotifier`

If you want to preview a notification for a particular format, you can use the -n (--notify) option from the command line.

`snotify --notify --format '%artist: %title'`

### 3.2 Playback control

Snotify also provides basic playback control with the -a option.

- toggle
- play
- pause
- next
- prev

### 3.3 Volume control

Use the --volume (-V) option to set volume.<br>
Possible values are [+/-] 0-100

### 3.4 Command line options

-h --help

-f --format=FORMAT text format

-n --notify - display notification

-F --force - force output to stdout

-a toggle,play,pause,next,prev - playback control

-V --volume=[+/-]volume_percent - set volume

-v --version

## 4. Uninstall

`pip uninstall snotify`

`rm -rf ~/.config/snotify`

Remove the **onevent** line in your spotifyd.conf file and restart Spotifyd.
