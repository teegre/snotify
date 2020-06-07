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

When you're done:

**At the top of the *snotifier* script**:

  ```shell
  SPOTIFY_CLIENT_ID="YOUR_CLIENT_ID"
  SPOTIFY_CLIENT_SECRET="YOUR_CLIENT_SECRET"
  export SPOTIFY_CLIENT_ID
  export SPOTIFY_CLIENT_SECRET
  ```
replace **YOUR_CLIENT_ID** and **YOUR_CLIENT_SECRET** by your own credentials.  
If you use a password manager like *pass* you can of course pass the command to the  
variables. For instance:

  ```shell
  SPOTIFY_CLIENT_ID="$(pass path/to/spotify_client_id)"
  ...
  ```

### 1.3 Install Snotify:

`python setup.py install --user`

Then make sure to change *snotifier* permissions:

  ```shell
  chmod 700 "$HOME"/.local/bin/snotifier
  ```

## 2. Configuration

Add this line to your Spotifyd config file (~/.config/spotifyd/spotifyd.conf):

`onevent = /home/username/.local/bin/snotifier`

*Note:  
~/.config/snotify directory is created when you first use snotify.  
It contains a cache directory that stores album images, and also a token file.*

Finally restart Spotifyd:

`systemctl --user restart spotifyd.service`

That's it. A notification should display on song start / change / stop.

### 3. Notification format

By default, Snotify displays "artist: track title".  
That said, if you want to change notification format, you have to modify the **snotifier** script to your likings:  

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
