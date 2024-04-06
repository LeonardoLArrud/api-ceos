from django.db import models

class Item(models.Model):
    name= models.CharField(max_length=150)
    tipoPokemon = models.CharField(max_length=150, default='SOME STRING')
    fraquezaPokemon = models.CharField(max_length=150, default='SOME STRING')
    created = models.DateTimeField(auto_now_add=True)
   
