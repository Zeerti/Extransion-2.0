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
def deleteDatabase():
    # TODO: Delete DB files
    
    # Directory to be created
    directory = 'databaseBackup'
    
    # Parent Directory path 
    parent_dir = cwd = os.getcwd()
    
    # Path 
    path = os.path.join(parent_dir, directory) 
    
    # Create the directory 
    try: 
        os.mkdir(path) 
        print("Directory '%s' created" %directory) 

        # if directory / file that is to be created already exists then 'FileExistsError' will be raised by os.mkdir() method 
        # Similarly, if the specified path is invalid 'FileNotFoundError' Error will be raised 

    except OSError as error: 
        print(error)

    # Define files to be moved
    sourceFile1 = 'pickle.db.dat'
    sourceFile2 = 'pickle.db.bak'
    sourceFile3 = 'pickle.db.dir'
    destDir =  directory

    # Move database files from the Extransion directory to newly created databaseBackup folder
    shutil.move(sourceFile1, destDir)
    shutil.move(sourceFile2, destDir)
    shutil.move(sourceFile3, destDir)

# deleteDatabase()