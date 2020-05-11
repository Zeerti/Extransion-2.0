import shelve

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

# Deletes existing db files
def deleteDatabase():
    # TODO: Delete DB files