@echo off
cd ..
call env\Scripts\activate.bat
py src/print-position.py
PAUSE