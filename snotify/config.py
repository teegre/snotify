from os import getenv

cid = getenv('SPOTIFY_CLIENT_ID')
cs = getenv('SPOTIFY_CLIENT_SECRET')

if not cid: cid = 'SPOTIFY_CLIENT_ID'
if not cs: cs  = 'SPOTIFY_CLIENT_SECRET'
