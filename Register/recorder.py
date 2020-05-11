from pynput import mouse 
from pynput import keyboard
# from dbHandler import saveToDatabase

class Recorder(): 
    def __init__(self):
        self.actions = []
        self.listenFlag = False
        self.recordingFlag = False

        # Event Listeners config
        self.mouseListener = mouse.Listener(on_click=self.appendToActions)
        self.keyboardListener = keyboard.Listener(on_press=self.recorderControls)
    
    # Ensure that the actions array is empty
    # Close listening threads
    def __del__(self):
        self.actions = []
        self.closeListeningThreads()

    # Write the current X, Y coords and pressed button for the mouse
    # To the temp DB array for later storage
    def appendToActions(self, x, y, button, pressed):
        if(not pressed and self.listenFlag == True):
            print(x, y, button, pressed)
            _x = x
            _y = y
            _button = button

            tempDict = { 
                'x': _x,
                'y': _y,
                'button': _button
            }

            self.actions.append(tempDict)
 
    # Begins the event handler listening
    # Listens to keyboard and mouse events
    def startListening(self):
        self.recordingFlag = True
        self.mouseListener.start()
        self.keyboardListener.start()
    
    # Toggles flag to enable/disable appendToActions()
    # When disabled, it will not write to the temp DB array
    # When enabled it will allow writing to temp DB array
    def recorderControls(self, key):
        
        # if(not self.listenFlag):
        #     pass
        # TODO: YELL THAT YOU ARE ABOUT TO RE-ENABLE RECORDING 
        
        if (key == keyboard.Key.space):
            print('Changing listneing Flag')
            self.listenFlag = not self.listenFlag

        if (key == keyboard.Key.esc):
            print('Killing listening threads')
            self.closeListeningThreads() 
            self.recordingFlag = False
 
    # Closes both event handler threads
    # listening to mouse and keyboard events
    # Once closed they cannot be just opened.
    # A new instance will need to be generated
    def closeListeningThreads(self):
        self.recordingFlag = False
        self.mouseListener.stop()
        self.keyboardListener.stop()

    def isRecording(self):
        return self.recordingFlag
    
    def getActions(self):
        return self.actions
        
    