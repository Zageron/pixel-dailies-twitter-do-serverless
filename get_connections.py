import os
import requests
from os.path import dirname, abspath
from dotenv import load_dotenv

path = dirname(abspath(__file__)) + "/.env"
load_dotenv(path)

application_id = os.getenv("DISCORD_APP_ID")
guild_id = os.getenv("DISCORD_GUILD_ID")
url = f"https://discord.com/api/v10/users/197739503551643658/connections"

token = os.getenv("DISCORD_BOT_TOKEN")
headers = {"Authorization": f"Bot {token}"}
r = requests.get(url, headers=headers)
print(r.content)
