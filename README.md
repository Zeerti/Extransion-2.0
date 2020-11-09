# Extransion
Automating BrinkPOS for testing purposes

## Releases
https://github.com/Zeerti/Extransion-2.0/releases

## Requirements
1. Windows 10
2. PyWinAuto
3. Eel
4. Pynput
5. PyInstaller (optional)
6. Browser: Firefox, Chrome, or Edge

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

### Recording Instructions
1. Set the Register.exe file
2. Hit the "Start Recording" button at the bottom
3. Recording can be paused at any time by hitting `space`
4. When you are done recording press `ESC` to stop.
5. *__Warning:__* If you do not hit ESC the playback file will not be recorded. You must hit escape when you are finished to write the database file out.

### Playback Instructions
1. Set the Register.exe file
2. Set the delay between each recorded action
    - Recommended minimum of 0.5 seconds
    - This is a required field
3. Set the number of times you want it to repeat
    - This is a required field
#### A playback can be canceled at any time by pressing `escape`





