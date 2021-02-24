from Scorify.scorecard.handleDB import *

def updateData(input_value):
	if input_value=="one":
		incre_By_Score(run=1,ball=1,wicket=0)
	elif input_value=="two":
		incre_By_Score(run=2,ball=1,wicket=0)
	elif input_value=="three":
		incre_By_Score(run=3,ball=1,wicket=0)
	elif input_value=="four":
		incre_By_Score(run=4,ball=1,wicket=0)
	elif input_value=="six":
		incre_By_Score(run=6,ball=1,wicket=0)
	elif input_value=="five":
		incre_By_Score(run=5,ball=1,wicket=0)
	elif input_value=="wide":
		incre_By_Score(run=1,ball=0,wicket=0)
	elif input_value=="dot":
		incre_By_Score(run=0,ball=1,wicket=0)
	elif input_value=="wicket":
		incre_By_Score(run=0,ball=1,wicket=1)
	elif input_value=="nb":
		incre_By_Score(run=1,ball=0,wicket=0)
	elif input_value=="undo":
		UNDO()

def updateOvers():
    obj=loadData()
    obj.overs=str(obj.balls//6)+"."+str(obj.balls%6)
    storeData(obj)

def incre_By_Score(run=0,ball=0,wicket=0):
	obj=loadData()
	obj.score+=run
	obj.balls+=ball
	obj.wicket+=wicket
	storeData(obj)
	updateOvers()
	
def UNDO():
	obj=loadData()
	obj.score+=0
	storeData(obj)
	updateOvers()
