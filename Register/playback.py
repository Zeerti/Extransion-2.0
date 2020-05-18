import dbHandler
import pywinauto
from time import sleep
from pywinauto.application import Application
from pynput import keyboard

class Playback():
    def __init__(self):
        # Grab DB and copy into local var
        self.actions = dbHandler.getDatabase(False)
        self.enablePlaybackFlag = False
        self.abortFlag = False

        # Keyboard event listener
        self.keyboardListener = keyboard.Listener(on_press=self.playControls)
        self.keyboardListener.start()

        # PyWinAuto object
        self.app = Application()
    
    # Handles pausing or shutting down playback
    def playControls(self, key):
        # Handle space key being pressed
        if (key == keyboard.Key.space):
            print(f'Changing listening flag: {self.enablePlaybackFlag}')
            self.enablePlaybackFlag = not self.enablePlaybackFlag
        
        # Handle escape key being pressed
        if (key == keyboard.Key.esc):
            print(f'Closing playback down')
            self.enablePlaybackFlag = False
            self.abortFlag = True
    
    # begins playback of DB file
    def startPlayback(self, exe, delay, loops):
        # TODO: Launch Brink
        # TODO: Validate DLG is accurate. Top Level window may not be accurate
        try:
            self.app.start(exe, timeout=60) # app = Application().start(r"c:\path\to\your\application -a -n -y --arguments")
            dlg = self.app.top_window()
            dlg2 = self.app['Register']
            dlg2.print_control_identifiers() 
        except NameError as err:
            print(f'Failed starting Brink\n\n{err}')
        except OSError as err:
            print(f'2Failed starting Brink\n\n{err}')
        except RuntimeError as err:
            print(f'3Failed starting Brink\n\n{err}')
        
        _tempActions = self.actions
        for loop in range(loops):
            if(self.abortFlag):
                return
            if(self.enablePlaybackFlag):
                for action in _tempActions:
                    if(self.abortFlag):
                        return
                    if(not self.enablePlaybackFlag):
                        while not self.enablePlaybackFlag:
                            if(self.abortFlag):
                                return
                            pass
                    
                    # TODO: Make mouse move and click
                    pywinauto.mouse.click(button='left', coords=(action['x'], action['y']))
                    sleep(delay)
                    print(f"{ action['x'] }, { action['y'] }")
            if(not self.enablePlaybackFlag):
                while not self.enablePlaybackFlag: # Waits until pause is disabled
                    if(self.abortFlag): # Ends playback if it was paused
                        return
                    pass
                
            # Pop action off from 
  
pb = Playback()

pb.startPlayback("C:\\Brink\\Pos\\Register.exe", 2, 5)

 
                          