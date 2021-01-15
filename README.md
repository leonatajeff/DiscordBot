# Collaborative Playlist Bot

Discord bot for creating collaborative playlists. This bot listens to a discord channel and adds spotify links found to a public playlist for your server.

Create a `.env` file within this directory with the following fields:

```
# .env

# Bot token
DISCORD_TOKEN={BOT DISCORD TOKEN}

# Channel to listen to
CHANNEL={STRING OF CHANNEL THE BOT WILL LISTEN TO}

#Spotipy information
SPOTIPY_CLIENT_ID={CLIENT_ID}
SPOTIPY_CLIENT_SECRET={Secret ID}
SPOTIPY_REDIRECT_URI={Redirect URI found on the dashboard}

#Spotify information
SPOTIFY_USERNAME={USERNAME}
PLAYLIST={PLAYLIST_URI}

```

## Commands:

`!help` Displays help

`!remove [track_URI]` Removes all instances of the track specified from the playlist.

`!get_playlist` returns the playlist.
