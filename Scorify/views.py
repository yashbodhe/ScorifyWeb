from django.shortcuts import render
from django.http import HttpResponse
from Scorify.teams import createTeam,storeData,loadData
def index(request):
	teamObj=createTeam()
	storeData(teamObj)
	increOne()
	increOne()
	increOne()
	teamObj=loadData()
	param={'team':teamObj}
	return render(request,'index.html',param)
def increOne():
	obj=loadData()
	obj.score+=1
	storeData(obj)
	