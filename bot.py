# bot.py
import os
import re

import discord
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

#Discord Infomration
TOKEN = os.environ['DISCORD_TOKEN']
CHANNEL = os.environ['CHANNEL']

#Spotipy Information
SPOTIPY_CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
SPOTIPY_CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']
SPOTIPY_REDIRECT_URI = os.environ['SPOTIPY_REDIRECT_URI']
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-public"))
playlist = os.environ['PLAYLIST']
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
                await message.channel.send("Song added!")
            except:
                await message.channel.send("Addition of song failed")
        elif re.match(r'^(!remove)', message.content):
            try:
                sp.user_playlist_remove_all_occurrences_of_tracks(sp.me(), playlist, [message.content])
                await message.channel.send("Removal successful")
            except:
                await message.channel.send("Removal failed")
        elif message.content == '!help':
            await message.channel.send("!remove [track_URL] removes tracks. \n Otherwise, just paste urls in here and it will be added")
        elif message.content == '!playlist':
            await message.channel.send(playlist)
        else:
            print(f'Message id {message.id} is not a spotify link')
        return

    return

client.run(TOKEN)
