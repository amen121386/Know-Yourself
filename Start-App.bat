@echo off
chcp 65001 >nul
title Know-Yourself Standalone App Launcher

:: Resolve absolute path
set "APP_DIR=%~dp0"
set "HTML_FILE=%APP_DIR%Know-Yourself.html"

:: Check Microsoft Edge
set "EDGE_EXE="
if exist "%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe" set "EDGE_EXE=%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe"
if not defined EDGE_EXE if exist "%ProgramFiles%\Microsoft\Edge\Application\msedge.exe" set "EDGE_EXE=%ProgramFiles%\Microsoft\Edge\Application\msedge.exe"
if not defined EDGE_EXE if exist "%LOCALAPPDATA%\Microsoft\Edge\Application\msedge.exe" set "EDGE_EXE=%LOCALAPPDATA%\Microsoft\Edge\Application\msedge.exe"
if not defined EDGE_EXE where msedge.exe >nul 2>&1 && set "EDGE_EXE=msedge.exe"

if defined EDGE_EXE (
    echo Launching Know-Yourself in Standalone App Mode [Edge]...
    start "" "%EDGE_EXE%" --app="file:///%HTML_FILE:\=/%" --window-size=1360,860
    exit /b 0
)

:: Check Google Chrome
set "CHROME_EXE="
if exist "%ProgramFiles%\Google\Chrome\Application\chrome.exe" set "CHROME_EXE=%ProgramFiles%\Google\Chrome\Application\chrome.exe"
if not defined CHROME_EXE if exist "%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe" set "CHROME_EXE=%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe"
if not defined CHROME_EXE if exist "%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe" set "CHROME_EXE=%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"
if not defined CHROME_EXE where chrome.exe >nul 2>&1 && set "CHROME_EXE=chrome.exe"

if defined CHROME_EXE (
    echo Launching Know-Yourself in Standalone App Mode [Chrome]...
    start "" "%CHROME_EXE%" --app="file:///%HTML_FILE:\=/%" --window-size=1360,860
    exit /b 0
)

:: Fallback: default browser
echo Opening Know-Yourself with default browser...
start "" "%HTML_FILE%"
exit /b 0
