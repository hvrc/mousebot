@echo off
REM Batch script to run the test runner with pytest.ini in config/

REM Set the working directory to the script's location
cd /d "%~dp0"

REM Run the Python test runner
python utilities\run.py

REM Pause so the window stays open after execution
pause
