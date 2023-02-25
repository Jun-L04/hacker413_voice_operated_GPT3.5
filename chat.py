import os
import json
import openai
#openai is marked as not being used, but it is
#solution was found here 
#https://stackoverflow.com/questions/74311275/modulenotfounderror-no-module-named-openai

#my OpenAI key
openai.api_key = "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"
print("ask away")

#restricts response length
usrInput = input() + "within 2 sentences"

#sets up an OpenAI completion model
#gets a response from model as an OpenAIObject
response = openai.Completion.create(
    model="text-davinci-003",
    prompt=usrInput,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6
)

# converts OpenAIObject to json-formatted string
modelResponseStr = json.dumps(response)

#converts json string to python object having the same data strucutre
pyModelObj = json.loads(modelResponseStr)

#accesses the response from GPT
text_value = pyModelObj['choices'][0]['text']

#tests by printing to terminal
print(text_value)


