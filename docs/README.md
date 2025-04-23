# ReviewSphere

Portal recenzji multimedialnych

---

## 1. Wprowadzenie

Projekt **„Portal recenzji multimedialnych”** to aplikacja webowa napisana w Pythonie z wykorzystaniem bazy danych MySQL. Umożliwia użytkownikom (recenzentom) dodawanie recenzji filmów, książek, gier itp., wzbogaconych o grafikę (okładki lub zrzuty ekranu). Zaawansowany system uprawnień definiuje role:

- **Recenzent**  
- **Moderator**  
- **Administrator**

---

## 2. Opis systemu

### Cel

Stworzyć nowoczesne, responsywne narzędzie do publikacji i moderacji recenzji multimedialnych.

### Główne moduły

- **Rejestracja i logowanie użytkowników**  
  Obsługa rejestracji, logowania oraz resetowania hasła.  
- **Formularz dodawania recenzji**  
  Możliwość pisania recenzji z dołączaniem obrazków (okładek, zrzutów ekranu).  
- **System oceniania (gwiazdki)**  
  Użytkownicy mogą przyznawać oceny w skali od 1 do 5 gwiazdek.  
- **Sekcja komentarzy**  
  Pod każdą recenzją znajduje się możliwość dodawania i przeglądania komentarzy.  
- **Panel moderacji**  
  Automatyczne wykrywanie i blokowanie wulgaryzmów oraz naruszeń regulaminu.  
- **Panel administratora**  
  Zarządzanie użytkownikami, rolami oraz moderacja treści.

---
## Jak uruchomić
1. `python -m venv .venv`
2. `. .venv/Scripts/activate`
3. `pip install -r requirements.txt`
4. `flask db upgrade`
5. `flask run`
