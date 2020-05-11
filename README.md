# Extransion
Automating BrinkPOS for testing purposes

## Releases
https://github.com/Zeerti/Extransion/releases

## Requirements
1. Windows 10
2. PyWinAuto
3. Eel
4. PyInstaller (optional)
5. Browser: Firefox, Chrome, or Edge

## Installing from source
1. Download and install Python 3.7+
    - https://www.python.org/downloads/releases/

2. Clone this repository and extract it
3. In CMD navigate to the root folder you just extracted and type in the following
    - `pip install -r requirements.txt`

4. Once installed launch with the following command
    - `python extransion.py`

## Guide to using Extransion
1. GUI runs via a browser
2. Upon launch there will be two prompts
    - Record and Playback
        - Record will allow the user to set the actions/presses
        - Playback will repeat the actions set in the record module
3. If you would like to reset the recorded actions, or remove a previous set of actions, press Delete.
    - This backs up any previous actions and zips the files to a new folder `backupDB.zip`

## F.A.Q
1. Q: Why am I getting an error about a missing DB file?
2. Q: Why isn't anything happening when I hit start?
3. Q: Resverved Question?



