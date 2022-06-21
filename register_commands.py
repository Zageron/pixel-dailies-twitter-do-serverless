import os
import requests
from os.path import dirname, abspath
from dotenv import load_dotenv

path = dirname(abspath(__file__)) + "/.env"
load_dotenv(path)

application_id = os.getenv("DISCORD_APP_ID")
guild_id = os.getenv("DISCORD_GUILD_ID")

# This is an example CHAT_INPUT or Slash Command, with a type of 1
json = {
    "name": "count",
    "type": 1,
    "description": "Count the number of Pixel Dailies you have completed.",
    "options": [{"type": 3, "name": "handle", "description": "Your twitter username."}],
}

token = os.getenv("DISCORD_BOT_TOKEN")
headers = {"Authorization": f"Bot {token}"}

# url = f"https://discord.com/api/v10/applications/{application_id}/guilds/{guild_id}/commands"
# r = requests.post(url, headers=headers, json=json)
# r = requests.get(url, headers=headers)

command_id = 988535387813183529
del_url = f"https://discord.com/api/v10/applications/{application_id}/guilds/{guild_id}/commands/{command_id}"
r = requests.delete(del_url, headers=headers)

print(r.content)
