from flask import Flask, request, jsonify
from chatbot import load_model, ask_chatbot

app = Flask(__name__)

SYSTEM_DATA = load_model()

@app.route('/ask', methods=['POST'])
def ask_endpoint():
    data = request.json
    
    if not data or 'question' not in data:
        return jsonify({"answer": "Błąd: Brak pytania w żądaniu."}), 400
        
    user_input = data.get('question')

    if not user_input.strip():
        return jsonify({"answer": "Nie wpisano pytania."})

    answer = ask_chatbot(user_input, SYSTEM_DATA)

    return jsonify({"answer": answer})

if __name__ == '__main__':
    print("Uruchamianie serwera Flask na http://localhost:5050 ...")
    # debug=True ułatwia szukanie błędów podczas developmentu (resetuje serwer przy zmianie kodu)
    app.run(port=5050, debug=False)