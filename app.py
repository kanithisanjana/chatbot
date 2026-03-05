import streamlit as st
import speech_recognition as sr
import requests
import pyttsx3

# Initialize speaker
engine = pyttsx3.init()
engine.setProperty("rate", 170)

def speak(text):
    engine.say(text)
    engine.runAndWait()

st.set_page_config(page_title="SANJU Voice Assistant")
st.title("🎙️ SANJU – Voice Assistant")

recognizer = sr.Recognizer()

# 🎤 VOICE INPUT
if st.button("🎤 Speak"):
    with sr.Microphone() as source:
        st.info("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        st.success(f"You said: {command}")

        res = requests.post(
            "http://localhost:8000/command",
            params={"command": command}
        )

        reply = res.json()["response"]
        st.write("🤖 SANJU:", reply)
        speak(reply)

    except sr.UnknownValueError:
        st.error("Sorry, I could not understand.")
        speak("Sorry, I could not understand.")

    except sr.RequestError:
        st.error("Network error.")
        speak("Network error")

# ⌨️ OPTIONAL TEXT INPUT
command_text = st.text_input("Or type a command")

if st.button("Send Text"):
    res = requests.post(
        "http://localhost:8000/command",
        params={"command": command_text}
    )
    reply = res.json()["response"]
    st.write("🤖 SANJU:", reply)
    speak(reply)