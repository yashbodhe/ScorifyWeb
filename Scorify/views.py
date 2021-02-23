from django.shortcuts import render
from django.http import HttpResponse
from Scorify.scorecard.teams import *
from Scorify.teams import *
def index(request):
	teamObj=createTeam()
	storeData(teamObj)
	teamObj=loadData()
	param={'team':teamObj}
	return render(request,'index.html',param)
def increOne():
	obj=loadData()
	obj.score+=1
	storeData(obj)
	