import pickle 
class Team:
    def __init__(self):
        self.teamname ="Team RED"
        self.score =0
        self.wicket=0
        self.balls=0
        self.overs="0.0"

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

def updateOvers():
    obj=loadData()
    obj.overs=str(obj.balls//6)+"."+str(obj.balls%6)
    storeData(obj)