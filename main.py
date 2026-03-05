from fastapi import FastAPI
import datetime
import wikipedia
import pyjokes
from wordhoard import dictionary as d
import pywhatkit

app = FastAPI(title="SANJU API")

def process_command(command: str):
    command = command.lower()

    if "play" in command:
        song = command.replace("play", "")
        pywhatkit.playonyt(song)
        return f"Playing {song} on YouTube"

    elif "hi" in command or "hello" in command:
        return "Hello, how are you?"

    elif "time" in command:
        return datetime.datetime.now().strftime('%I:%M %p')

    elif "date" in command:
        return str(datetime.date.today())

    elif "day" in command:
        return datetime.date.today().strftime("%A")

    elif "who is" in command:
        try:
            return wikipedia.summary(command.replace("who is", ""), sentences=1)
        except:
            return "Sorry, I couldn't find that."

    elif "define" in command:
        try:
            return str(d(command.replace("define", "")).meanings())
        except:
            return "Definition not found."

    elif "joke" in command:
        return pyjokes.get_joke()

    else:
        return "Sorry, I don’t understand yet."

@app.post("/command")
def handle_command(command: str):
    return {"response": process_command(command)}