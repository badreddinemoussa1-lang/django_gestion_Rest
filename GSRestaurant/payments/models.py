from django.db import models
from orders.models import Commande


# Create your models here.

class Facture(models.Model):
    commande = models.OneToOneField(Commande, on_delete=models.CASCADE, related_name='facture')
    dateFacture = models.DateTimeField(auto_now_add=True)
    montantTotal = models.FloatField()

    def __str__(self):
        return f"Facture #{self.id} - Commande #{self.commande.id}"

class Paiement(models.Model):
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE, related_name='paiements')
    modePaiement = models.CharField(max_length=50) 
    datePaiement = models.DateTimeField(auto_now_add=True)
    montant = models.FloatField() 

    def __str__(self):
        return f"Paiement de {self.montant} pour factue{self.facture.id}"