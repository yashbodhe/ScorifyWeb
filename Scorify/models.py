from django.db import models 
from django.db.models import Model 

# Create your models here.
class ScoreCardModel(Model):
    # other fields 
    data = models.TextField()