import requests
import json
import botogram

with open("key.json", "r") as f:
    key = json.load(f)["key"]

print(f"{key}")
bot = botogram.create(key)
@bot.command("hello")
def hello_command(chat, message, args):
    """Say hello to the world!"""
    chat.send("Hello world")


if __name__ == "__main__":
    bot.run()
