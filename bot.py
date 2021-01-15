# bot.py
import os
import discord
import re
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

#Discord Infomration
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL = os.getenv('CHANNEL')

#Spotipy Information
SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-public"))
playlist = os.getenv('PLAYLIST')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.channel.name == CHANNEL:
        # inside of desired channel
        if re.match(r'^(http(s)*://open.spotify.com/track/)', message.content):
            try:
                sp.user_playlist_remove_all_occurrences_of_tracks(sp.me(), playlist, [message.content])
                sp.playlist_add_items(playlist, [message.content])
                print("Song added!")
            except:
                print("Addition of song failed")
        else:
            print(f'Message id {message.id} is not a spotify link')
        return

    return

client.run(TOKEN)