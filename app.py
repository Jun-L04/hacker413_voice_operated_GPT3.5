from dotenv import load_dotenv
import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

load_dotenv()
#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "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"


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        userInput = request.form["userInput"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_chat(userInput),
            temperature=0.5,
            max_tokens=39,
            top_p=0.3,
            frequency_penalty=0.5,
            presence_penalty=0
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_chat(userInput):
    return "yay"
