@echo off
setlocal enabledelayedexpansion

:: Specify the path to your file
set "playlists=D:\usr\noHat\bin\playlists"
set "playlinks=D:\usr\noHat\bin\playlinks"

:: Check if the file exists
if not exist "%playlists%" (
    echo File does not exist: %playlists%
    exit /b 1
)

:: Initialize the increment variable
set /a i=1

:: Read the file line by line
for /f "usebackq tokens=* delims=" %%A in ("%playlists%") do (
    echo List!i! : %%A
    :: Increment the variable
    set /a i+=1
)
set /a i-=1
:: Prompt the user for input
echo:

set /p "userInput=Enter a Playlsit You Wanna Listen : "

:: Validate the input to ensure it's a number
echo %userInput%| findstr /r /c:"^[0-9]*$" >nul
if errorlevel 1 (
    echo Invalid input. Please enter a valid number.
    exit /b 1
)

:: Process the numerical input
@REM echo You entered: %userInput%
:: Compare userInput Playlist Number exceeds total Number of Playlist Available, if so display Unavailable message and return
if %userInput% gtr %i% (     
    echo Only !i! Playlists are Available...
    exit /b 1
) else (
    set /a i=1
    :: Read the file line by line
    for /f "usebackq tokens=* delims=" %%A in ("%playlinks%") do (
        
        if %userInput% equ !i! (
            echo Opening .......
            brave -incognito %%A
            echo Opened, Go check your Browser..
        )
        
        :: Increment the variable
        set /a i+=1
)
)

echo done

endlocal
