from django.db import models

class Avis(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    poste = models.CharField(max_length=100)
    message = models.TextField()

    def save_to_database(self):
        self.save()

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
    def save_to_database(self):
        self.save()