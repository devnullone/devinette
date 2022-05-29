from django.db import models

# Create your models here.

class Level (models.Model):
    levelName = models.CharField(max_length = 200)
    limit = models.IntegerField()


class Joueur (models.Model):
    nom = models.CharField(max_length = 200)


class Score (models.Model):
    joueur = models.ForeignKey(Joueur, related_name='Score', on_delete=models.CASCADE)
    score = models.IntegerField()

class Devinette (models.Model):
    devinette = models.CharField(max_length= 255)
    reponse = models.CharField(max_length= 200)

class Chiffre (models.Model):
    chiffre_adeviner = models.IntegerField()