import json
import os
from discord_interactions import (
    verify_key,
    InteractionType,
    InteractionResponseType,
)


def fail():
    return {
        "statusCode": 401,
    }


def main(args):
    PUBLIC_KEY = os.getenv("DISCORD_PUB_KEY")

    print(f"Arguments: {args}")  # debug print

    body = args.get("__ow_body")
    headers = args.get("__ow_headers")
    if body is None or headers is None:
        return fail()

    signature = headers.get("x-signature-ed25519")
    timestamp = headers.get("x-signature-timestamp")
    if (
        signature is None
        or timestamp is None
        or not verify_key(body.encode(), signature, timestamp, PUBLIC_KEY)
    ):
        return fail()

    body_json = json.loads(body)
    if body_json.get("type") == InteractionType.PING:
        return {
            "body": {"type": InteractionResponseType.PONG},
            "statusCode": 200,
        }
    elif body_json.get("type") == InteractionType.APPLICATION_COMMAND:
        print("APPLICATION_COMMAND")
        return {
            "body": {
                "type": InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
                "data": {"content": "Hello, you interacted with a component."},
            },
            "statusCode": 200,
        }
