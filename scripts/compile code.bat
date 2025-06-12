@echo off
call env\Scripts\activate
set /p "file=Enter file name to compile: "
pyinstaller --onedir --add-data="drag_images/*;drag_images/" --add-data="templates/*;templates/" %file%
PAUSE

