# **Snotify** version 1.0 (05-2020)

**Snotify** is a simple notification tool for Spotifyd written in Python 3.

*Dependencies: dunst (or similar)*

## 1. Installation

### 1.1 Clone this repository:

`git clone https://github.com/teegre/snotify.git`

### 1.2 Client ID and Secret

To be able to use snotify, you need to get your own *client id* and *client secret*.  
Go to: [https://developer.spotify.com/dashboard/](https://developer.spotify.com/dashboard/)  and connect.  
Then click on **"create a client id"** and follow the instructions.

When you're done, modify the file **snotify/config.py**:

  ```python
  if not cid: cid = 'YOUR_CLIENT_ID'
  if not cs: cs = 'YOUR_CLIENT_SECRET'
  ```

### 1.3 Install Snotify:

`python setup.py install --user`

## 2. Configuration

Add this line to your Spotifyd config file (~/.config/spotifyd/spotifyd.conf):

`onevent = /home/username/.local/bin/snotify`

*Note: A configuration file named token will be stored in ~/.config/snotify/*

Finally restart Spotifyd:

`systemctl --user restart spotifyd.service`

That's it. A notification should display on song start / change / stop.

### 3 Notification format

You can specify what to display by using the -f (--format) option. For instance :

`snotify -f '%artist: %title'`  
or  
`snotify -i -f $'%title\n%artist\n%album | %year'`

Possible variables are:

|Variable |Description
|:--------|:----------
|%artist |artist name
|%title |track title
|%album |album
|%year |year of release

By default, Snotify displays "artist: track title".  
That said, if you want to change notification format, you have to use the included **snotifier** script  
(copy it somewhere and modify it) and change the **onevent** option in the Spotifyd configuration file accordingly, ie:

`onevent = /home/username/bin/snotifier`

### 4 Command line options

-h --help

-f --format=FORMAT text format

-i --image - display album art in notification

-F --force - force output to stdout

-v --version

## 4. Uninstall

Use the script included:

`./uninstall.sh`

Remove the **onevent** line in your spotifyd.conf file and restart Spotifyd.
