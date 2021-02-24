import pickle 
  
def storeData(obj): 
    # initializing data to be stored in db 
    
    # database 
    db = {} 
    db['team1'] = obj 
      
    # Its important to use binary mode 
    dbfile = open('localDB', 'wb')       
    # source, destination 
    pickle.dump(db, dbfile)   
                   
    dbfile.close() 

def loadData(): 
    # for reading also binary mode is important 
    dbfile = open('localDB', 'rb')      
    db = pickle.load(dbfile) 
    teamObj=db['team1'] 
    dbfile.close() 
    return teamObj
