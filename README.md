Pour ce challenge il y a plusieurs étapes :

# Côté création :
1. créer un venv sous Windows `python3.7 -m venv .venv`
2. activer le venv `.\venv\Scripts\activate`
3. installer pyinstaller `pip3.7 install pyinstaller`
4. compiler le code `pyinstaller --onefile main.py -w`

# Côté résolution
1. télécharger https://github.com/extremecoders-re/pyinstxtractor
2. exécuter le code `python3.7 .\pyinstextractor.py .\dist\main.exe`
3. télécharger https://github.com/andrew-tavera/unpyc37
4. décompiler le code avec `python3.7 .\decompyle.py .\main.exe_extracted\PYZ-00.pyz_extracted\modules\keylogger.pyc > keylogger.py`
