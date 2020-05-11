import dbHandler
from recorder import Recorder
import eel
# import playback # Not created yet


######################## 
#  Recorder Assembler  #
########################
@eel.expose
def startRecording(): 
        print('Grabbing DB')
        db = dbHandler.getDatabase()
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
    # TODO: Finish playback assembly
    # playback = Playback(delay,)
    pass


# dbHandler.getDatabase()
# dbHandler.createDatabase()  
# startRecording()

    
