import pickle 

class Team:
	def __init__(self):
		self.teamname ="team1"
		self.score =100
		self.wicket=3
		self.overs=4

def createTeam():
	t=Team()
	return t

  
def storeData(obj): 
    # initializing data to be stored in db 
  
    # database 
    db = {} 
    db['team1'] = obj 
      
    # Its important to use binary mode 
    dbfile = open('examplePickle', 'wb') 
    s_obj = serializers.serialize("json", [obj]) # convert object to json format          
    obj2 = ScoreCardModel.objects.create(data=s_obj)
    obj2.save()
    # source, destination 
    pickle.dump(db, dbfile)                      
    dbfile.close() 
  
def loadData(): 
    # for reading also binary mode is important 
    dbfile = open('examplePickle', 'rb')      
    db = pickle.load(dbfile) 
    teamObj=db['team1'] 
    dbfile.close() 
    return teamObj