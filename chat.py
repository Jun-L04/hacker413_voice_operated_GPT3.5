import os
from gtts import gTTS
import json
from audioTranscribe import answers
import startRecording
import openai
# openai is marked as not being used, but it is
# solution was found here
# https://stackoverflow.com/questions/74311275/modulenotfounderror-no-module-named-openai

# ---Initialization--- #
# my OpenAI key (DO NOT LEAK)
openai.api_key = "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"


# ---Functions--- #
def clean_gpt_response(response):
    # converts OpenAIObject to json-formatted string
    modelResponseStr = json.dumps(response)
    # converts json string to python object having the same data strucutre
    pyModelObj = json.loads(modelResponseStr)
    # accesses the response from GPT
    text_value = pyModelObj['choices'][0]['text']
    return text_value

def speaking(response):
    spokenResponse = clean_gpt_response(response)
    print(spokenResponse)
    language = 'en'
    myobj = gTTS(text=spokenResponse, lang=language, slow=False)
    myobj.save("latestResponse.mp3")
    os.system("mpg321 latestResponse.mp3")


# ---Ready to Answer--- #
exampleAudio = "I will be ready soon, please wait"
language = 'en'
myobj = gTTS(text=exampleAudio, lang=language, slow=False)
myobj.save("readying.mp3")
os.system("mpg321 readying.mp3")

# ---Endless Loop of Voice Assisting--- #
while True:
    #restricts input length
    usrInput = answers + "within 2 sentences"
    
    # gets a response from model as an OpenAIObject
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=usrInput,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6
    )
    speaking(response)
    #tests by printing to terminal
    # print(clean_gpt_response(response) + "\n")
    break


"""
Sample input: "repeat after me: I like thicc booty mommies"

Sample output: "I enjoy looking at round and curvy booty mommies. They make me feel tingly inside!"

"""

# TODO
# concatenate usrinput strings together so GPT knows context
# maybe put it in an array and add each one


# TODO
# separate into different methods


# TODO
# make this repetitive, don't stop after one iteration