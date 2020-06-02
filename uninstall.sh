#! /usr/bin/env sh
pip uninstall snotify
rm -rf build dist snotify.egg-info snotify/__pycache__
rm -f ~/.local/bin/snotify
rm -f ~/.local/bin/snotifier
rm -rf ~/.config/snotify
