from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import nltk
from knowledge_base import knowledge_base
import wikipedia

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

# -------------------------
# KNOWLEDGE BASE
# -------------------------

knowledge_base = {
    "who is father of the nation":
        "Mahatma Gandhi is commonly referred to as the Father of the Nation in India.",

    "who is india's prime minister":
        "Narendra Modi is the Prime Minister of India.",

    "who is narendra modi":
        "Narendra Modi is an Indian politician serving as the Prime Minister of India.",

    "what is artificial intelligence":
        "Artificial Intelligence (AI) is a branch of computer science that enables machines to perform tasks that normally require human intelligence.",

    "what is machine learning":
        "Machine Learning is a subset of Artificial Intelligence that enables systems to learn from data and improve automatically.",

    "hello":
        "Hello! How can I help you today?",

    "hi":
        "Hi! How can I assist you?",

    "good morning":
        "Good morning! Hope you're having a great day.",

    "good evening":
        "Good evening! How can I assist you today?"
}

# -------------------------
# AI MODEL
# -------------------------

MODEL_NAME = "google/flan-t5-base"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

def get_wikipedia_answer(query):
    try:
        return wikipedia.summary(query, sentences=3)
    except:
        return None

def ai_response(user_input):

    prompt = f"""
    You are an intelligent AI assistant.

    Rules:
    - Give accurate answers.
    - If unsure, say 'I don't know'.
    - Do not invent facts.

    Question: {user_input}

    Answer:
    """

    inputs = tokenizer(prompt, return_tensors="pt")

    outputs = model.generate(
        **inputs,
        max_new_tokens=100
    )

    response = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return response


def generate_response(user_input):

    query = user_input.lower().strip()

    if query in knowledge_base:
        return knowledge_base[query]

    wiki_answer = get_wikipedia_answer(user_input)

    if wiki_answer:
        return wiki_answer

    return ai_response(user_input)
