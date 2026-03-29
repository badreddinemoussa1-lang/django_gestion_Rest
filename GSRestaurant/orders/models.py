from django.db import models
from account.models import Utilisateur
from tablesRestaurant.models import TablesRestaurant
from menu.models import Plat


# Create your models here.

class Commande(models.Model):
    Utilisateur=models.ForeignKey(Utilisateur,on_delete=models.SET_NULL,null=True,related_name='commandes_creees')
    table=models.ForeignKey(TablesRestaurant,on_delete=models.CASCADE,null=True,related_name='commmandes')
    dateCommande=models.DateField(auto_now=True)
    statut=models.CharField(max_length=100)
    total=models.DecimalField(max_digits=10,decimal_places=10,default=0.00)

    def __str__(self):
        return f"Commandes{self.id} -Tables{self.table.numero}"


class LigneCommande(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE, related_name='lignes')
    plat = models.ForeignKey(Plat, on_delete=models.CASCADE)
    quantite = models.IntegerField()
    prixUnitaire = models.DecimalField(max_digits=10, decimal_places=2)
    sousTotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantite}x {self.plat.nom}"






