from django import forms
from produits.models import Produit

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit  # Définir le modèle associé
        fields = ['nom','description', 'prix']  # Spécifier les champs du formulaire
