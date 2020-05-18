import shelve
import os
import shutil
from datetime import date


# Returns the current db file AS A COPY
# You will need to explicityly resave it with the saveToDatabase function
# automatically will close DB with False passed.
# Leaves DB file open for writing if True is passed
def getDatabase(recordFlag):
    db = shelve.open('pickle.db')
    if(recordFlag):
        return db
    else:
        try:
            # Make a copy of the DB and then close it
            _dbCopy = db['actions']
            db.close()

            return _dbCopy
        except KeyError as err:
            # TODO: Callback function stating DB is empty
            print(f'DB is empty. Cannot return an empty DB\n\n {err}')
            db.close()

        
        

# Generates a shelve object with the name pickle.db
# Contains one key value pair as an example of structure
# returns newly created DB
def createDatabase():
    _db = shelve.open('pickle.db')
    return _db
    

# Takes in an array of dictionarys
# Each dictionary should only contain a x and y key
# their values should ONLY be integers.
def saveToDatabase(db, actions):
    db['actions'] = actions
    print(f'Saved {actions} to database')
    db.close()

# Moves existing db files to backup folder
def backupDatabase():
    # TODO: Backup DB files
    
    # Directory to be created
    # import today's date for backup folder naming
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

