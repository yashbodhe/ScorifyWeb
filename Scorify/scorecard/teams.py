import pickle 
class Team:
    def __init__(self):
        self.teamname ="Team RED"
        self.score =0
        self.wicket=0
        self.overs=0

def createTeam():
    t=Team()
    return t

  
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