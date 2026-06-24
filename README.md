# E.D.E.K. (Eksperymentalny Doradca Emitujący Komunikaty)

E.D.E.K. to lekki, nowoczesny chatbot typu *Question Answering* oparty na technologii **Sentence Transformers**. Projekt stanowi hybrydę wydajnego backendu w języku Python oraz minimalistycznego, responsywnego frontendu opartego na PHP, HTML i CSS.

## 🧠 Jak działa E.D.E.K.?

Silnik bota wykorzystuje **wyszukiwanie semantyczne (Semantic Search)**:
1. **Analiza wektorowa:** Pytania użytkownika są konwertowane na wektory liczbowe przy użyciu modelu wielojęzycznego `paraphrase-multilingual-MiniLM-L12-v2`.
2. **Podobieństwo:** System oblicza podobieństwo cosinusowe pomiędzy zapytaniem a pytaniami w bazie (`cosine_similarity`).
3. **Inteligentna odpowiedź:** Jeśli podobieństwo przekracza zdefiniowany próg (`threshold = 0.5`), E.D.E.K. serwuje dopasowaną odpowiedź.

## 🛠 Architektura systemu

- **Frontend (`index.php`, `style.css`, `script.js`):** Interfejs użytkownika komunikujący się z backendem za pomocą asynchronicznych zapytań `fetch`. Wspiera tryb jasny/ciemny zapisywany w `localStorage`.
- **Backend AI (`main.py`, `chatbot.py`):** Serwer Flask (Python), który przyjmuje pytania przez endpoint `/ask` i zwraca odpowiedzi w formacie JSON.
- **Data Pipeline (`bake_mode.py`):** Moduł przygotowawczy, który "piecze" (konwertuje) bazę wiedzy JSON do postaci numerycznej (wektorów), co pozwala na natychmiastowe uruchomienie bota bez czekania na przeliczenia przy każdym starcie.

## 🚀 Instrukcja instalacji i uruchomienia

### 1. Przygotowanie środowiska
Upewnij się, że masz zainstalowane wymagane biblioteki:
```bash
pip install flask sentence-transformers scikit-learn numpy

```

### 2. Przygotowanie bazy danych

1. Przygotuj plik `baza_wiedzy.json` z Twoimi pytaniami i odpowiedziami w formacie:
`{"Pytanie?": "Odpowiedź."}`.
2. Uruchom skrypt przygotowawczy:

```bash
   python bake_mode.py

```

*To wygeneruje plik `upieczone_wektory.npy`.*

### 3. Start systemu

1. **Backend:** Uruchom serwer Flask:

```bash
   python main.py

```

2. **Frontend:** Umieść pliki webowe na serwerze PHP (np. XAMPP/WAMP). Upewnij się, że w `index.php` adres zapytań `fetch` wskazuje na poprawny port (domyślnie `5050`).

## ❓ Przykładowe pytania dla bota

* "Jak masz na imię?"
* "Czy umiesz programować?"
* "Kto cię stworzył?"
* "Opowiedz mi o silnikach parowych." (przy założeniu posiadania bazy SQuAD)

## 📋 Wskazówki techniczne

* **Dataset:** Aby dodać nową wiedzę, edytuj `mdoel_dataset.json` i uruchom ponownie `bake_mode.py`.
* **Port:** Jeśli port `5050` jest zajęty, zmień go zarówno w `main.py` jak i w pliku `index.php`.
* **Tryb pracy:** Bot wymaga aktywnego serwera Flask w tle, aby zwracać odpowiedzi.

---