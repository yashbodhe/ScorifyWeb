from django.shortcuts import render
from Scorify.scorecard.handleTeams import *
from Scorify.scorecard.updateScorecard import *

def index(request):
	return render(request,'index.html')

def initScore(request):
	teamObj=createTeam()
	teamObj.teamname=request.POST['team1']
	storeData(teamObj)
	teamObj=loadData()
	param={'team':teamObj}
	return render(request,'scorecard.html',param)

def getData(request):
	input_value=request.POST['inputValue']
	updateData(input_value)
	teamObj=loadData()
	param={'team':teamObj}
	return render(request,'scorecard.html',param)
	