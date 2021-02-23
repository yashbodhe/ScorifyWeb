from django.shortcuts import render
from django.http import HttpResponse
from Scorify.scorecard.teams import *
from Scorify.scorecard.updateScorecard import *
def index(request):
	teamObj=createTeam()
	storeData(teamObj)
	teamObj=loadData()
	param={'team':teamObj}
	return render(request,'index.html',param)

def getData(request):
	input_value=request.POST['inputValue']
	if input_value=="one":
		incre_By_One()
	elif input_value=="two":
		incre_By_Two()
	elif input_value=="three":
		incre_By_Three()
	elif input_value=="four":
		incre_By_Four()
	elif input_value=="six":
		incre_By_Six()
	elif input_value=="five":
		incre_By_Five()
	elif input_value=="wide":
		incre_By_Wide()
	elif input_value=="dot":
		incre_By_Dot()
	elif input_value=="wicket":
		incre_By_Wicket()
	elif input_value=="nb":
		incre_By_NB()
	elif input_value=="undo":
		incre_By_UNDO()
	teamObj=loadData()
	param={'team':teamObj}
	print("Hello getData")
	return render(request,'index.html',param)
	