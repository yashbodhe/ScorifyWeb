from Scorify.scorecard.handleDB import *
class Team:
    def __init__(self):
        self.flag=True
        self.winner=None
        self.overs=1
        self.team1=["Team1",0,0,0,"0.0"]
        self.team2=["Team2",0,0,0,"0.0"]
        #["TeamName",TeamRuns,TeamWickets,TeamBalls,"TeamOvers"]

def createTeam():
    t=Team()
    return t

def check_innOver(obj):
    if obj.flag:
        if obj.team1[2]==10 or obj.team1[3]==obj.overs*6:
            obj.flag=False
    else:
        if obj.team2[2]==10 or obj.team2[3]==obj.overs*6:
            if obj.team1[1]>obj.team2[1]:
                obj.winner="Team1"
            elif obj.team1[1]<obj.team2[1]:
                obj.winner="Team2"
            else:
                obj.winner="YASH"
    return obj