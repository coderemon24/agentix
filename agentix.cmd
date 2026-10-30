@ECHO off
SETLOCAL EnableDelayedExpansion

:: 1. Check if scripts\agx.py exists in current directory
IF EXIST "%CD%\scripts\agx.py" (
    python "%CD%\scripts\agx.py" %*
    EXIT /B %ERRORLEVEL%
)

:: 2. Walk up parent directories to find scripts\agx.py
SET "CURR_DIR=%CD%"
:loop
IF EXIST "!CURR_DIR!\scripts\agx.py" (
    python "!CURR_DIR!\scripts\agx.py" %*
    EXIT /B !ERRORLEVEL!
)
SET "PARENT_DIR="
FOR %%I IN ("!CURR_DIR!\..") DO SET "PARENT_DIR=%%~fI"
IF "!PARENT_DIR!"=="" GOTO notfound
IF "!PARENT_DIR!"=="!CURR_DIR!" GOTO notfound
SET "CURR_DIR=!PARENT_DIR!"
GOTO loop

:notfound
:: 3. If scripts\agx.py is next to this batch file
IF EXIST "%~dp0scripts\agx.py" (
    python "%~dp0scripts\agx.py" %*
    EXIT /B %ERRORLEVEL%
)

ECHO [AGENTIX] Error: 'scripts\agx.py' not found in current directory or parent folders.
ECHO Run 'irm https://raw.githubusercontent.com/coderemon24/agentix/main/install.ps1 | iex' to install Agentix in this project.
EXIT /B 1
