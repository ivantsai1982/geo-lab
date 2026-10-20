@echo off
chcp 65001 >nul
cd /d "%~dp0"
start "" http://localhost:8765/
echo Website running at http://localhost:8765/
echo Close this window to stop it.
python -m http.server 8765 --directory website
