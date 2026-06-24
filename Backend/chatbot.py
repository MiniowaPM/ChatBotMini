from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import json

def load_model():
    print("Ładowanie modelu AI ...")
    model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
    
    with open('model_dataset.json', 'r', encoding='utf-8') as f:
        qa_database = json.load(f)

    questions = list(qa_database.keys())

    question_embeddings = np.load('model_dataset.npy')
    print("Model załadowany pomyślnie!")

    return {
        "model": model,
        "qa_database": qa_database,
        "questions": questions,
        "question_embeddings": question_embeddings
    }

def ask_chatbot(user_input: str, system_data: dict, threshold: float = 0.5) -> str:
    model = system_data["model"]
    question_embeddings = system_data["question_embeddings"]
    questions = system_data["questions"]
    qa_database = system_data["qa_database"]

    user_emb = model.encode(user_input)
    
    scores = cosine_similarity([user_emb], question_embeddings)[0]

    best_index = np.argmax(scores)
    best_score = scores[best_index]

    if best_score >= threshold:
        return qa_database[questions[best_index]]
    else:
        return "Nie znalazłem odpowiedzi na to pytanie. Sformułuj je inaczej."