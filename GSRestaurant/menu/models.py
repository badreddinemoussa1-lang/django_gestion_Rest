from django.db import models

# Create your models here.
class CategoriePlat(models.Model):
    nomcategorie=models.CharField(max_length=100)

    def __str__(self):
        return self.nomcategorie
    
class Plat(models.Model):
    categorie = models.ForeignKey(CategoriePlat, on_delete=models.CASCADE, related_name='plats')
    nom = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField()
    prix = models.FloatField() 

    def __str__(self):
        return self.nom