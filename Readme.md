# 🤖 Intelligent AI Assistant

An AI-powered conversational assistant built using **Python, FastAPI, Transformers, NLTK, SQLite, HTML, CSS, and JavaScript**. The application leverages Natural Language Processing (NLP) and Transformer-based language models to generate intelligent responses, maintain conversation history, and provide a seamless chat experience through a web interface.

---

# 📌 Overview

The Intelligent AI Assistant is designed to interact with users in natural language, understand queries, and generate meaningful responses using advanced NLP techniques.

The project demonstrates:

* Natural Language Processing (NLP)
* Transformer-based AI models
* REST API development using FastAPI
* Database integration using SQLite
* Frontend-Backend communication
* Conversational AI applications

---

# 🚀 Features

* 💬 Real-time AI conversations
* 🧠 Transformer-based response generation
* 📚 Natural Language Processing (NLP)
* ⚡ FastAPI REST API
* 🗄️ SQLite chat history storage
* 🎨 Interactive web interface
* 🔄 Dynamic frontend-backend communication
* 📜 Conversation logging
* 🌐 Scalable architecture

---

# 🛠️ Tech Stack

## Backend

* Python
* FastAPI
* Transformers (Hugging Face)
* NLTK
* SQLite

## Frontend

* HTML5
* CSS3
* JavaScript

## Database

* SQLite

---

# 📂 Project Structure

```text id="s2v32i"
AI_CHATBOT_PROJECT/
│
├── backend/
│   ├── app.py
│   ├── chatbot.py
│   ├── database.py
│   ├── chatbot.db
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash id="qj6nly"
git clone https://github.com/yourusername/intelligent-ai-assistant.git
cd intelligent-ai-assistant
```

## Install Dependencies

```bash id="73obgo"
pip install -r requirements.txt
```

Or

```bash id="l31x5k"
py -m pip install fastapi uvicorn transformers torch nltk python-multipart
```

---

# ▶️ Running the Application

Navigate to backend directory:

```bash id="swmxyt"
cd backend
```

Start FastAPI server:

```bash id="iwxjlwm"
py -m uvicorn app:app --reload
```

Server URL:

```text id="nzh87g"
http://127.0.0.1:8000
```

API Documentation:

```text id="uq5ycn"
http://127.0.0.1:8000/docs
```

---

# 🌐 Frontend

Open:

```text id="x5zt9c"
frontend/index.html
```

or use VS Code Live Server.

---

# 📡 API Endpoints

## Home Endpoint

```http id="gq8pqk"
GET /
```

Response:

```json id="lyp3zq"
{
  "message": "AI Assistant Running"
}
```

---

## Chat Endpoint

```http id="7r4ml8"
POST /chat
```

Request:

```json id="i13vk9"
{
  "message": "What is Artificial Intelligence?"
}
```

Response:

```json id="d5vv7k"
{
  "user_message": "What is Artificial Intelligence?",
  "bot_response": "Artificial Intelligence is a field of computer science focused on creating systems capable of performing tasks that typically require human intelligence."
}
```

---

## Chat History

```http id="c0h8zz"
GET /history
```

Returns all previous conversations stored in SQLite.

---

# 🗄️ Database Schema

## chat_logs

| Field        | Type     |
| ------------ | -------- |
| id           | INTEGER  |
| user_message | TEXT     |
| bot_response | TEXT     |
| timestamp    | DATETIME |

---

# 🔍 System Workflow

```text id="7z6r9q"
User Input
     ↓
Frontend Interface
     ↓
FastAPI Backend
     ↓
NLP Processing
     ↓
Transformer Model
     ↓
AI Response Generation
     ↓
Store Conversation in SQLite
     ↓
Return Response to User
```

---

# 🎯 Applications

* AI Assistants
* Virtual Assistants
* Educational Chatbots
* Information Retrieval Systems
* NLP Learning Projects
* Conversational AI Research
* Intelligent Help Desk Systems

---

# 📸 Screenshots

Add screenshots of:

* Home Page
* Chat Interface
* API Documentation
* Chat History

Example:

```text id="g4hpt5"
screenshots/chat-interface.png
```

---

# 📈 Future Enhancements

* Voice Interaction
* Speech-to-Text Integration
* Text-to-Speech Responses
* Multi-language Support
* User Authentication
* Personalized Conversations
* Sentiment Analysis
* Knowledge Base Integration
* OpenAI/Gemini API Support
* AI Agent Capabilities

---

# 🎓 Learning Outcomes

This project demonstrates practical implementation of:

* Natural Language Processing (NLP)
* Conversational AI
* FastAPI Development
* REST APIs
* Database Management
* Frontend-Backend Integration
* Transformer Models
* AI Application Development

---

# 👨‍💻 Author

**Sanjana K**

B.Tech Student | AI & Machine Learning Enthusiast

GitHub: https://github.com/yourusername

LinkedIn: https://linkedin.com/in/yourprofile

---

# ⭐ If you found this project useful, consider giving it a star on GitHub!
