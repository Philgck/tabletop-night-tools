from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Boardgame List Model. The intent of this model is to update the database with a personalised list of games. 

class AddGame(models.Model):
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    review = models.TextField(blank=True, null=True)
    minimum_player_count = models.IntegerField()
    maximum_player_count = models.IntegerField()
    image_url = models.URLField(blank=True, null=True)    