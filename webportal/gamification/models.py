from django.db import models

class Game(models.Model):
    game_name = models.CharField(max_length = 100)
    game_description = models.CharField(max_length = 250)