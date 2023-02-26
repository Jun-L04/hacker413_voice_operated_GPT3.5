import os
import json
import openai
# openai is marked as not being used, but it is
# solution was found here
# https://stackoverflow.com/questions/74311275/modulenotfounderror-no-module-named-openai

# my OpenAI key (DO NOT LEAK)
openai.api_key = "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"
#print("ask away")

# restricts response length
#usrInput = input() + "within 2 sentences"


def gpt_answer(response):
    # converts OpenAIObject to json-formatted string
    modelResponseStr = json.dumps(response)
    # converts json string to python object having the same data strucutre
    pyModelObj = json.loads(modelResponseStr)
    # accesses the response from GPT
    text_value = pyModelObj['choices'][0]['text']
    return text_value

usrConcate = ""

while True:
    print("ask away")
    usrInput = input() + "within 2 sentences"
    usrConcate = usrConcate + usrInput
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=usrConcate,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6
    )
    print(gpt_answer(response))
    print("X to exit")
    exitInput = input()
    if exitInput == "X":
        break
# TODO
# concatenate usrinput strings together so GPT knows context
# maybe put it in an array and add each one


# TODO
# separate into different methods


# TODO
# make this repetitive, don't stop after one iteration


# sets up an OpenAI completion model
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


'''def gpt_answer(response):
    # converts OpenAIObject to json-formatted string
    modelResponseStr = json.dumps(response)
    # converts json string to python object having the same data strucutre
    pyModelObj = json.loads(modelResponseStr)
    # accesses the response from GPT
    text_value = pyModelObj['choices'][0]['text']
    return text_value'''

# tests by printing to terminal
print(gpt_answer(response))
