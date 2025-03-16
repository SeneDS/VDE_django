from django.db import models
from django.utils import timezone

# Create your models here.
#ici on crée la table Produit qui a pour chants: nom, description et prix. Cette table herite de la calsse modele.
#Pour faire apparettre cete table dans l'interface admin il faut faire la migration
class Produit(models.Model):
    nom          = models.CharField(blank=False,  null=False, max_length=220)
    description = models.TextField(blank=True,  null=True, default="pase de description")
    prix        = models.DecimalField(blank=False,  null=False,max_digits=10000, decimal_places=2)
    active      = models.BooleanField(blank=True)
    is_deleted = models.BooleanField(blank=True, default=False)
    date = models.DateTimeField(blank=False, default=timezone.now)
