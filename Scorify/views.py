from django.shortcuts import render
from Scorify.scorecard.handleTeams import *
from Scorify.scorecard.updateScorecard import *
from django.http import HttpResponse
import random

def index(request):
	params={"toss":False, "win":None}
	return render(request,'index.html',params)

def toss(request):
	opt = ["Team 1 won the Toss","Team 2 won the Toss"]
	win=random.choice(opt)
	params={"toss":True, "win":win}
	return render(request,'index.html',params)

def matchDetails(request):
	return render(request,'matchDetails.html')

def initScore(request):
	teamObj=createTeam()
	
	if request.POST['toss']=="team1":
		teamObj.team1[0]=request.POST['team1']
		teamObj.team2[0]=request.POST['team2']
	else:
		teamObj.team2[0]=request.POST['team2']
		teamObj.team1[0]=request.POST['team1']
	teamObj.overs=int(request.POST['overs'])
	storeData(teamObj)
	teamObj=loadData()
	
	param={'match':teamObj}
	return render(request,'scorecard.html',param)

def getData(request):
	input_value=request.POST['inputValue']
	updateData(input_value)
	
	teamObj=loadData()
	
	param={'match':teamObj}
	if teamObj.winner!=None:
		return render(request,'summary.html',param)
	return render(request,'scorecard.html',param)
	