# ReviewSphere 🎬

ReviewSphere to aplikacja do dodawania i oceniania recenzji z możliwością komentowania, głosowania oraz moderacji.

## Wymagania

- Python 3.10+
- pip (Python package manager)
- XAMPP (z Apache + MySQL)
- phpMyAdmin (do łatwego zarządzania bazą danych)

## Konfiguracja środowiska

1. Zainstaluj [XAMPP](https://www.apachefriends.org/index.html) i uruchom serwery Apache oraz MySQL.
2. Otwórz `phpMyAdmin` (`http://localhost/phpmyadmin`) i stwórz bazę danych o nazwie `reviewsphere_db`.
3. Skonfiguruj połączenie z bazą danych w pliku `config.py`, np.:

```python
SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/reviewsphere_db'


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
