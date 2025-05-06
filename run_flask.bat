@echo off
cd /d "E:\psoc notes\sensei"
start "" py app.py
timeout /t 3 >nul
start http://127.0.0.1:5000

