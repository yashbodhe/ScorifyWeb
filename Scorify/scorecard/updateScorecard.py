from Scorify.scorecard.handleDB import *
from Scorify.scorecard.handleTeams import *

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
    match=loadData()
    if match.flag:
    	match.team1[4]=str(match.team1[3]//6)+"."+str(match.team1[3]%6)
    else:
    	match.team2[4]=str(match.team2[3]//6)+"."+str(match.team2[3]%6)
    match=check_innOver(match)
    storeData(match)

def incre_By_Score(run=0,ball=0,wicket=0):
	match=loadData()
	if match.flag:
		match.team1[1]+=run
		match.team1[2]+=wicket
		match.team1[3]+=ball
	else:
		match.team2[1]+=run
		match.team2[2]+=wicket
		match.team2[3]+=ball
	storeData(match)
	updateOvers()
	
def UNDO():
	pass
