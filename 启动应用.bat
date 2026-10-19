@echo off
title Know-Yourself 本地独立外脑工作台

:: 获取当前目录
set "APP_DIR=%~dp0"
set "HTML_FILE=%APP_DIR%Know-Yourself.html"

:: 优先检测 Microsoft Edge 常用安装路径
set "EDGE_EXE="
if exist "%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe" set "EDGE_EXE=%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe"
if not defined EDGE_EXE if exist "%ProgramFiles%\Microsoft\Edge\Application\msedge.exe" set "EDGE_EXE=%ProgramFiles%\Microsoft\Edge\Application\msedge.exe"
if not defined EDGE_EXE if exist "%LOCALAPPDATA%\Microsoft\Edge\Application\msedge.exe" set "EDGE_EXE=%LOCALAPPDATA%\Microsoft\Edge\Application\msedge.exe"
if not defined EDGE_EXE where msedge.exe >nul 2>&1 && set "EDGE_EXE=msedge.exe"

if defined EDGE_EXE (
    echo [OK] 正在以独立 App 模式启动 Know-Yourself [基于 Edge 核心]...
    start "" "%EDGE_EXE%" --app="file:///%HTML_FILE:\=/%" --window-size=1360,860
    exit /b 0
)

:: 次选 Google Chrome
set "CHROME_EXE="
if exist "%ProgramFiles%\Google\Chrome\Application\chrome.exe" set "CHROME_EXE=%ProgramFiles%\Google\Chrome\Application\chrome.exe"
if not defined CHROME_EXE if exist "%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe" set "CHROME_EXE=%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe"
if not defined CHROME_EXE if exist "%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe" set "CHROME_EXE=%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"
if not defined CHROME_EXE where chrome.exe >nul 2>&1 && set "CHROME_EXE=chrome.exe"

if defined CHROME_EXE (
    echo [OK] 正在以独立 App 模式启动 Know-Yourself [基于 Chrome 核心]...
    start "" "%CHROME_EXE%" --app="file:///%HTML_FILE:\=/%" --window-size=1360,860
    exit /b 0
)

:: 兜底：使用系统默认浏览器直接打开
echo [OK] 正在使用默认浏览器打开 Know-Yourself...
start "" "%HTML_FILE%"
exit /b 0
