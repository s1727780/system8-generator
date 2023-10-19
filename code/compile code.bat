@echo off
call env\Scripts\activate
set /p "file=Enter file name to compile: "
pyinstaller --windowed  --onefile %file%
PAUSE