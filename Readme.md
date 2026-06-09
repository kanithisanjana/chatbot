# 🤖 Intelligent AI Assistant

An AI-powered conversational assistant built using **Python, FastAPI, Transformers, NLTK, SQLite, HTML, CSS, and JavaScript**. The assistant combines a Knowledge Base, Wikipedia-based information retrieval, and Transformer-based Natural Language Processing (NLP) to provide accurate and intelligent responses to user queries.

---

# 📌 Project Overview

The Intelligent AI Assistant is designed to simulate human-like conversations while maintaining factual accuracy through a hybrid architecture.

Unlike traditional chatbots that rely solely on AI-generated responses, this project uses:

- Knowledge Base Retrieval
- Wikipedia Information Retrieval
- Transformer-based Response Generation
- Chat History Logging

This hybrid approach improves answer quality, reduces hallucinations, and provides more reliable responses.

---

# 🚀 Features

- 💬 Real-time conversational AI
- 📚 Knowledge Base for predefined accurate responses
- 🌐 Wikipedia-powered information retrieval
- 🧠 Transformer-based NLP response generation
- ⚡ FastAPI REST API backend
- 🗄️ SQLite database integration
- 📜 Chat history storage and retrieval
- 🎨 Interactive and responsive web interface
- 🔄 Dynamic frontend-backend communication
- 🔍 Intelligent query routing

---

# 🛠️ Tech Stack

## Backend

- Python
- FastAPI
- Transformers (Hugging Face)
- NLTK
- Wikipedia API
- SQLite

## Frontend

- HTML5
- CSS3
- JavaScript

## Database

- SQLite

---

# 📂 Project Structure

```text
AI_CHATBOT_PROJECT/
│
├── backend/
│   ├── app.py
│   ├── chatbot.py
│   ├── knowledge_base.py
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

# 🏗️ System Architecture

```text
User Query
    ↓
Knowledge Base Search
    ↓
Answer Found?
 ├─ Yes → Return Accurate Answer
 │
 └─ No
      ↓
Wikipedia Information Retrieval
      ↓
Information Found?
 ├─ Yes → Return Retrieved Information
 │
 └─ No
      ↓
Transformer Model (FLAN-T5)
      ↓
Generate Intelligent Response
      ↓
Store Chat History
      ↓
Return Response
```

---

# ⚙️ Installation

## Clone the Repository

```bash
git clone https://github.com/yourusername/intelligent-ai-assistant.git

cd intelligent-ai-assistant
```

---

## Install Required Packages

```bash
pip install -r requirements.txt
```

or

```bash
py -m pip install fastapi uvicorn transformers torch nltk wikipedia python-multipart
```

---

# ▶️ Running the Backend

Navigate to backend directory:

```bash
cd backend
```

Start FastAPI server:

```bash
py -m uvicorn app:app --reload
```

Server URL:

```text
http://127.0.0.1:8000
```

API Documentation:

```text
http://127.0.0.1:8000/docs
```

---

# 🌐 Running the Frontend

Open:

```text
frontend/index.html
```

or

Use VS Code Live Server:

```text
Right Click → Open with Live Server
```

---

# 📡 API Endpoints

## Home Endpoint

### Request

```http
GET /
```

### Response

```json
{
    "message": "AI Assistant Running"
}
```

---

## Chat Endpoint

### Request

```http
POST /chat
```

### Request Body

```json
{
    "message": "What is Artificial Intelligence?"
}
```

### Response

```json
{
    "user_message": "What is Artificial Intelligence?",
    "bot_response": "Artificial Intelligence is a branch of computer science focused on creating intelligent systems capable of performing tasks that normally require human intelligence."
}
```

---

## Chat History Endpoint

### Request

```http
GET /history
```

### Response

Returns all previous chat conversations stored in SQLite.

---

# 🗄️ Database Schema

## chat_logs

| Field | Type |
|---------|---------|
| id | INTEGER |
| user_message | TEXT |
| bot_response | TEXT |
| timestamp | DATETIME |

---

# 🔍 NLP Workflow

```text
User Input
     ↓
Text Preprocessing
     ↓
Knowledge Base Lookup
     ↓
Wikipedia Retrieval
     ↓
Transformer-Based NLP
     ↓
Response Generation
     ↓
Database Logging
     ↓
Return Response
```

---

# 🎯 Applications

- Intelligent Virtual Assistants
- Educational AI Assistants
- Question Answering Systems
- Knowledge Retrieval Systems
- Conversational AI Applications
- NLP Learning Projects
- Information Assistance Tools
- AI Research Demonstrations

---

# 📸 Screenshots

## Chat Interface

Add your chatbot screenshots here:

```text
screenshots/chat-interface.png
```

## API Documentation

```text
screenshots/api-docs.png
```

## Chat History

```text
screenshots/chat-history.png
```

---

# 📈 Future Enhancements

- 🎙️ Voice Input Support
- 🔊 Text-to-Speech Responses
- 🌍 Multi-language Support
- 🔐 User Authentication
- 😊 Sentiment Analysis
- 📄 Chat Export to PDF
- 🌙 Dark Mode
- 🧠 Context-Aware Conversations
- 🔎 Real-Time Web Search Integration
- 🤖 AI Agent Functionality

---

# 🎓 Learning Outcomes

This project demonstrates practical implementation of:

- Natural Language Processing (NLP)
- Conversational AI
- Transformer Models
- FastAPI Development
- REST API Design
- Database Management using SQLite
- Information Retrieval Systems
- Frontend-Backend Integration
- Hybrid AI Architectures
- Intelligent Response Generation

---

# 🌟 Key Highlights

- Hybrid Knowledge Base + Wikipedia + AI Architecture
- Reduced Hallucination Compared to Traditional Chatbots
- Faster Responses for Frequently Asked Questions
- Improved Accuracy Through Information Retrieval
- Scalable and Modular Design

---

# 👨‍💻 Author

**Sanjana K**

B.Tech Student | Artificial Intelligence & Machine Learning Enthusiast

GitHub: https://github.com/yourusername

LinkedIn: https://linkedin.com/in/yourprofile

---

# 📄 License

This project is developed for educational and learning purposes.

---

# ⭐ Support

If you found this project useful, please consider giving it a star ⭐ on GitHub.
Your support helps improve and maintain the project.
