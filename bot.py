import discord
import requests
import json
import datetime, time
from discord.ext import commands

client = discord.Client()

client = commands.Bot(command_prefix = '!')


@client.command()
async def phonelookup(ctx, *, phonenum):
    r       = requests.get(f"https://api.numlookupapi.com/v1/validate/{phonenum}?apikey=") # Get an api key from numlookupapi.com and paste it there
    plookup     = r.json()
    em      = discord.Embed(color=000000)
    fields  = [ 
        {'name': 'Valid:',          'value': plookup['valid']},
        {'name': 'Number:',     'value': plookup['number']},
        {'name': 'Local Format:',     'value': plookup['local_format']},
        {'name': 'International Format:',        'value': plookup['international_format']},
        {'name': 'Country prefix:',   'value': plookup['country_prefix']},
        {'name': 'Country Code:',     'value': plookup['country_code']},
        {'name': 'Country Name:',         'value': plookup['country_name']},
        {'name': 'Location',    'value': plookup['location']},
        {'name': 'Linetype:',   'value': plookup['line_type']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=True)

    em.set_footer(text='\u200b')
    em.timestamp = datetime.datetime.utcnow()  
    em.set_footer(text='Made By ocryol#8123')
    await ctx.send(embed = em)

client.run("TOKEN HERE")
