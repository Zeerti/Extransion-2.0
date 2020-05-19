import dbHandler
from recorder import Recorder
from playback import Playback  
import eel
# import playback # Not created yet


######################## 
#  Recorder Assembler  #
########################
@eel.expose
def startRecording():
        # TODO: Start Brink 
        print('Grabbing DB')
        db = dbHandler.getDatabase(True)
        isRecording = True
        print('Loading recording software')
        recorder = Recorder()
        print('Listening to events...')
        recorder.startListening()  

        # Loop and do nothing
        # Waiting until recording is done
        while isRecording:
            if (not recorder.isRecording()):
                isRecording = False # Exit while loop
                recorder.closeListeningThreads() # Shutdown recording threads
                actions = recorder.getActions() # Retreive all recorded actions 
                dbHandler.saveToDatabase(db, actions) # Save recorded actions to the DB
                

  
########################
#  Playback Assembler  #
########################
@eel.expose
def startPlayback():
    playback = Playback()
    # TODO: Finish playback assembly
    # PATH needs to be linked with GUI
    playback.startPlayback('C:\\Brink\\Pos\\Register.exe', 0.02, 5)
        


# dbHandler.getDatabase()
# dbHandler.createDatabase()  
# startRecording()

    
