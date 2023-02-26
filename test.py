#TEST FILE
#NOT AN ACTIVE PART OF THE PROJECT (YET)

import openai
import os

# Set up your OpenAI API key
openai.api_key = "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"

# Create a stateful conversation
conversation_id = None


def send_message(message):
    global conversation_id
    if conversation_id is None:
        # Start a new conversation if there is no conversation_id
        response = openai.Completion.create(
            engine="davinci",
            prompt="",
            max_tokens=0,
            n=1,
            stop=None,
            frequency_penalty=0,
            presence_penalty=0,
            response_format="json",
            stream=True,
        )
        conversation_id = response["id"]
    # Send a message to the existing conversation
    response = openai.Completion.create(
        engine="davinci",
        prompt=message,
        temperature=0.7,
        max_tokens=1024,
        n=1,
        stop=None,
        frequency_penalty=0,
        presence_penalty=0,
        response_format="json",
        stream=True,
        stream_id=conversation_id,
    )
    # Get the response text and set the conversation_id for the next request
    text = response["choices"][0]["text"]
    conversation_id = response["id"]
    return text
