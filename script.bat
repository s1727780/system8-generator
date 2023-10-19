@ECHO OFF
set /p "id=Enter Project Number: "

if exist %id%\ (
	echo Project folder already exists
	PAUSE
) else (
	echo Copying Files
	xcopy /v /q /i /s "Testflow Template" %id%
	ren %id%\"Template Testflow.tfl" %id%" Testflow.tfl"
	PAUSE
) 
