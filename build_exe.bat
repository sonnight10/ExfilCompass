@echo off
rem Construit ExfilCompass.exe : UN SEUL fichier, sans Python requis chez l'utilisateur.
rem Prérequis : Python 3.12 ou 3.13 installé (pas de version préliminaire). Lance ce fichier par double-clic depuis ce dossier.
python -m pip install -r requirements.txt pyinstaller
python -m PyInstaller --noconfirm --clean --onefile --windowed --name ExfilCompass --icon assets\icon.ico ^
  --add-data "exfilcompass\ui;exfilcompass\ui" ^
  --add-data "exfilcompass\data;exfilcompass\data" ^
  main.py
echo.
echo Termine : dist\ExfilCompass.exe  (ce fichier unique suffit, tu peux le donner tel quel)
pause
