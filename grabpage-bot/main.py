import os
import json.decoder
import re
import Flask

BOT_NAME = "grabpage-bot"
IMGUR_CLIENT_KEY = ""

def make_response(text):

    return aiohttp.web.json_response(
        data={
            "bot": "grabpage-bot",
            "text": text
        },
        status=201
    )


def find_urls(text):

    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)

    return urls


def start_app()

    app = Flask("grabpage-bot")


if __name__ == "__main__":

    pass