from django.db import models

# Create your models here.
class TablesRestaurant(models.Model):
    numero=models.IntegerField(unique=True)
    capacite=models.IntegerField()
    etat=models.CharField(max_length=100)

    def __str__(self):
        return self.numero,self.capacite,self.etat

