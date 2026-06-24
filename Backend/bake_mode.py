import json
import numpy as np
from sentence_transformers import SentenceTransformer

def convert_squad(plik_squad, plik_wynikowy):
    with open(plik_squad, 'r', encoding='utf-8') as f:
        squad = json.load(f)
    
    baza = {}
    for temat in squad['data']:
        for paragraf in temat['paragraphs']:
            for qas in paragraf['qas']:
                # Bierzemy tylko te pytania, które mają poprawne odpowiedzi
                if qas['answers']:
                    baza[qas['question']] = qas['answers'][0]['text']
    
    with open(plik_wynikowy, 'w', encoding='utf-8') as f:
        json.dump(baza, f, ensure_ascii=False, indent=4)

convert_squad('model_dataset.json', 'model_dataset.json')

print("Wczytywanie modelu...")
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

with open('model_dataset.json', 'r', encoding='utf-8') as f:
    qa_data = json.load(f)

questions = list(qa_data.keys())

print(f"Rozpoczynam wypiek wektorów dla {len(questions)} pytań...")
embeddings = model.encode(questions)

np.save('model_dataset.npy', embeddings)
print("Gotowe! Plik 'model_dataset.npy' zapisany.")