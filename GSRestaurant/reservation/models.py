from django.db import models
from tablesRestaurant.models import TablesRestaurant

# Create your models here.

class Reservation(models.Model):
    table=models.ForeignKey(TablesRestaurant,on_delete=models.CASCADE,related_name='reservations')
    nomClient=models.CharField(max_length=100)
    telephone=models.IntegerField()
    dateReservation=models.DateField()
    nbPersonnes=models.IntegerField()
    statut=models.CharField(max_length=100)
    def __str__(self):
        return self.nomClient,self.telephone,self.dateReservation,self.nbPersonnes,self.Statut
    
