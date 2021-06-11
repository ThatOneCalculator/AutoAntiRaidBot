import asyncio
import codecs
import datetime
import time
import humanfriendly
import io
import itertools
import json
import logging
import math
import os
import pprint
import random
import re
import shutil
import string
import subprocess
import sys
import threading
import traceback
import typing
import urllib.parse
import urllib.request

from io import StringIO
from typing import Any
from typing import Iterable
from typing import Tuple

import aiofiles
import aiohttp
import discord
import requests

from async_timeout import timeout
from discord import AsyncWebhookAdapter
from discord import RequestsWebhookAdapter
from discord import Webhook
from discord.ext import commands
from discord.ext import tasks

url_rx = re.compile(r'https?://(?:www\.)?.+')
upsince = datetime.datetime.now()

intents = discord.Intents.default()
intents.members = True
bot = commands.AutoShardedBot(command_prefix="!", description="Anti-raid bot made by ThatOneCalculator#1337", intents=intents, chunk_guilds_at_startup=True)

class SussyMogus(commands.Cog):

	@commands.Cog.listener()
	async def on_member_join(self, member):
		await bot.wait_until_ready()
		if "h0nda" in member.name:
			await member.ban()
		now = datetime.datetime.now()
		diff = now - member.created_at
		if diff.total_seconds() < 86400:
			await member.send("Due to an influx of raids, your account has been deemed to young to join this server.")
			await member.kick()

	@commands.command()
	async def literallynobot(self, ctx):
		"""Directs you to ThatOneCalculator's main bot"""

		await ctx.send("https://top.gg/bot/646156214237003777")

	@commands.command()
	async def github(self, ctx):
		"""Directs you to the GitHub repository for this bot."""

		await ctx.send("https://github.com/ThatOneCalculator/AntiSpamBot")

@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Activity(
		type=discord.ActivityType.watching,
		name=f"anti-spam on {len(bot.guilds)} servers!}"
	))
	print("Logged in!")


def read_token():
	with open("token.txt", "r") as f:
		lines = f.readlines()
		return lines[0].strip()

token = read_token()

bot.add_cog(SussyMogus(bot))

bot.run(token)
print("Logged in!")
