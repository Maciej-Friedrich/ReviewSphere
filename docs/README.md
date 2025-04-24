
# ReviewSphere 🎬🌟

ReviewSphere to aplikacja webowa do publikowania, oceniania i komentowania recenzji z wbudowanym systemem ról, moderacją treści oraz trybem ciemnym.

## 🔧 Wymagania

- Python 3.10+
- Virtualenv
- XAMPP (zalecane do lokalnej bazy danych MySQL i phpMyAdmin)

## 🚀 Instalacja

1. **Klonuj repozytorium**

```bash
git clone https://github.com/TwojaNazwaUzytkownika/ReviewSphere.git
cd ReviewSphere
```

2. **Utwórz środowisko wirtualne i aktywuj je**

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

3. **Zainstaluj zależności**

```bash
pip install -r requirements.txt
```

4. **Skonfiguruj bazę danych z XAMPP**

- Uruchom XAMPP i włącz moduł **MySQL**.
- Przejdź do [phpMyAdmin](http://localhost/phpmyadmin).
- Utwórz nową bazę danych: `reviewsphere_db`.

5. **Dodaj plik `config.py`**

```python
class Config:
    SECRET_KEY = 'twoj-sekret'
    SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost/reviewsphere_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

6. **Zainicjalizuj bazę danych**

```bash
flask db init
flask db migrate
flask db upgrade
```

7. **Uruchom aplikację**

```bash
flask run
```

Aplikacja dostępna będzie pod `http://localhost:5000`.

## 📷 Zrzuty ekranu

(dodaj tutaj obrazy GUI: strony recenzji, komentarzy, panel admina)

## 👥 Role użytkowników

- `recenzent`: podstawowy użytkownik z możliwością dodawania recenzji i komentowania
- `moderator`: może edytować/usunąć komentarze innych
- `admin`: pełna kontrola, możliwość zmiany ról

## 🔒 System głosowania i moderacji

- Głosowanie na komentarze (↑/↓), 1 głos na użytkownika
- Ostrzeganie i ukrywanie komentarzy zawierających wiele wulgaryzmów
- Edycja i usuwanie recenzji/komentarzy przez właścicieli i moderatorów

## 🌙 Tryb ciemny

- Możliwość przełączania trybu ciemnego przez dropdown menu użytkownika
- Preferencje zapisywane w `localStorage`

## 📂 Struktura katalogów

```
ReviewSphere/
│
├── app/
│   ├── templates/
│   ├── static/
│   ├── views/
│   ├── models.py
│   ├── forms.py
│   └── ...
├── migrations/
├── config.py
├── requirements.txt
└── README.md
```

## 📃 Licencja

Projekt stworzony w celach edukacyjnych.
