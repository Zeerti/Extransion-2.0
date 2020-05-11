import shelve
import os
import shutil


# Returns the current db file AS A COPY
# You will need to explicityly resave it with the saveToDatabase function
def getDatabase():
    # TODO: Finish Function
    db = shelve.open('pickle.db')
    print( db['actions'] )
    return db

# Generates a shelve object with the name pickle.db
# Contains one key value pair as an example of structure
# Should only need to be done once
def createDatabase():
    _db = shelve.open('pickle.db')
    _db['actions'] = [
        {
            'x': '0',
            'y': '0'
        },
        {
            'x': '1',
            'y': '1'
        }
    ]
    

# Takes in an array of dictionarys
# Each dictionary should only contain a x and y key
# their values should ONLY be integers.
def saveToDatabase(db, actions):
    db['actions'] = actions
    db.close()

# Moves existing db files to backup folder
def backupDatabase():
    # TODO: Backup DB files
    
    # Directory to be created
    # import today's date for backup folder naming
    from datetime import date
    today = date.today()

    directory = ('DatabaseBackup'+today.strftime("-%b-%d-%Y"))
    
    # Parent Directory path 
    parent_dir = cwd = os.getcwd()
    
    # Path 
    path = os.path.join(parent_dir, directory) 

    # Define files to be moved
    sourceFile1 = 'pickle.db.dir'
    sourceFile2 = 'pickle.db.bak'
    sourceFile3 = 'pickle.db.dat'

    from zipfile import ZipFile
    # create a ZipFile object
    with ZipFile('backupDB.zip', 'w') as zipObj:

        #create complete filepath of file in directory
        path = os.path.join(parent_dir, directory)

        # Add file to zip
        zipObj.write(sourceFile1)
        zipObj.write(sourceFile2)
        zipObj.write(sourceFile3)
    
    # Delete original db files from Extransion folder
    os.remove('pickle.db.dir')
    os.remove('pickle.db.bak')
    os.remove('pickle.db.dat')

backupDatabase()
# createDatabase()