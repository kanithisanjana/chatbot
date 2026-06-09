from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import nltk

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

model_name = "google/flan-t5-base"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def generate_response(user_input):

    prompt = f"""
    You are an intelligent customer support assistant.

    Rules:
    - Give accurate answers.
    - If unsure, say you don't know.
    - Do not invent facts.
    - Keep answers concise.

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