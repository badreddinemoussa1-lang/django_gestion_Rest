from django.db import models

# Create your models here.
class Role(models.Model):
    nomRole=models.CharField(max_length=50)

    def __str__(self):
        return self.nomRole
    
class Utilisateur(models.Model):
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, related_name='utilisateurs')
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    motDePasse = models.CharField(max_length=255) 

    def __str__(self):
        return f"{self.prenom} {self.nom}"