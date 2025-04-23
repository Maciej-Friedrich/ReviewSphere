# start.ps1 — uruchomienie środowiska i serwera Flask

Write-Host "🔁 Uruchamiam środowisko wirtualne..."
. .\.venv\Scripts\Activate.ps1

Write-Host "⚙️ Ustawiam zmienne środowiskowe..."
$env:FLASK_APP = "run.py"
$env:FLASK_ENV = "development"

Write-Host "🚀 Uruchamiam serwer Flask..."
flask run
