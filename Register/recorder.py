from pynput import mouse 
from pynput import keyboard
# from dbHandler import saveToDatabase

class Recorder(): 
    def __init__(self):
        self.actions = []
        self.listenFlag = True
        self.mouseListener = mouse.Listener(on_click=self.appendToActions)
        self.mouseListener.start()

        self.keyboardListener = keyboard.Listener(on_press=self.toggleListening)
        self.keyboardListener.start()
    
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
        
    # Current design will force program to be restarted if listeners are stopped
    # need to add in a flag to have it just ignore the listener 
    def toggleListening(self, key):
        if(not self.listenFlag){
            # TODO: YELL THAT YOU ARE ABOUT TO RE-ENABLE RECORDING
        }
        if (key == Key.esc){
            self.listenFlag = not self.listenFlag
        }
    
rec = Recorder() 
while True:
    a = 7