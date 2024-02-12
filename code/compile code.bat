@echo off
call env\Scripts\activate
set /p "file=Enter file name to compile: "
pyinstaller --onefile --add-data="drag_images/*;drag_images/" %file%
PAUSE