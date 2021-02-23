from Scorify.scorecard.teams import *

def incre_By_One():
	obj=loadData()
	obj.score+=1
	obj.balls+=1
	storeData(obj)
	updateOvers()
def incre_By_Two():
	obj=loadData()
	obj.score+=2
	obj.balls+=1
	storeData(obj)
	updateOvers()
def incre_By_Three():
	obj=loadData()
	obj.score+=3
	obj.balls+=1
	storeData(obj)
	updateOvers()
def incre_By_Four():
	obj=loadData()
	obj.score+=4
	obj.balls+=1
	storeData(obj)
	updateOvers()
def incre_By_Six():
	obj=loadData()
	obj.score+=6
	obj.balls+=1
	storeData(obj)
	updateOvers()
def incre_By_Five():
	obj=loadData()
	obj.score+=5
	obj.balls+=1
	storeData(obj)
	updateOvers()
def incre_By_Wide():
	obj=loadData()
	obj.score+=1
	storeData(obj)
	updateOvers()
def incre_By_Dot():
	obj=loadData()
	obj.score+=0
	obj.balls+=1
	storeData(obj)
	updateOvers()
def incre_By_Wicket():
	obj=loadData()
	obj.wicket+=1
	obj.balls+=1
	storeData(obj)
	updateOvers()
def incre_By_NB():
	obj=loadData()
	obj.score+=1
	storeData(obj)
	updateOvers()
def incre_By_UNDO():
	obj=loadData()
	obj.score+=0
	storeData(obj)
	updateOvers()
