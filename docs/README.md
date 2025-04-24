# ReviewSphere 🎬

ReviewSphere to aplikacja do dodawania i oceniania recenzji z możliwością komentowania, głosowania oraz moderacji.

## 🔧 Wymagania
- Python 3.10+
- Virtualenv
- MySQL lub SQLite (domyślnie SQLite)

## 🚀 Instalacja i uruchomienie

```bash
# 1. Klonuj repozytorium
git clone https://github.com/uzytkownik/ReviewSphere.git
cd ReviewSphere

# 2. Utwórz środowisko wirtualne
python -m venv venv
source venv/bin/activate    # lub .\venv\Scripts\activate na Windows

# 3. Zainstaluj zależności
pip install -r requirements.txt

# 4. Utwórz bazę danych
flask db upgrade

# 5. Uruchom aplikację
flask run
