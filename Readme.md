# 🎙️ SANJU – Voice Assistant

A simple **Python Voice Assistant** built using **FastAPI (Backend)** and **Streamlit (Frontend)**.

It supports:
- 🎤 Voice Commands
- ⌨️ Text Commands
- 🕒 Time & Date
- 📖 Wikipedia Search
- 📚 Word Definitions
- 😂 Random Jokes
- ▶️ Play Songs on YouTube

---

# 🏗️ Project Structure

```
sanju-voice-assistant
│
├── backend
│   ├── main.py
│   └── requirements.txt
│
├── frontend
│   ├── app.py
│   └── requirements.txt
│
└── README.md
```

---

# 🚀 Installation

## 1. Clone Repository

```
git clone https://github.com/yourusername/sanju-voice-assistant.git
cd sanju-voice-assistant
```

---

# 🔧 Backend Setup

```
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend will run at:

```
http://localhost:8000
```

---

# 💻 Frontend Setup

Open another terminal:

```
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

Frontend will run at:

```
http://localhost:8501
```

---

# 🎯 Example Commands

| Command | Result |
|-------|-------|
| hello | Greeting |
| time | Current Time |
| date | Today's Date |
| day | Current Day |
| who is Elon Musk | Wikipedia Info |
| define computer | Dictionary Meaning |
| joke | Random Joke |
| play shape of you | Plays song on YouTube |

---

# 🧠 Technologies Used

- Python
- FastAPI
- Streamlit
- SpeechRecognition
- pyttsx3
- Wikipedia
- pywhatkit
- pyjokes
- wordhoard

---

# ⚠️ Important

Make sure the **backend is running before starting frontend**.

Also allow **microphone access** for voice commands.

---

# 👩‍💻 Author

**Sanjana Kanithi**

---

⭐ If you like this project, consider giving it a **star on GitHub**!
