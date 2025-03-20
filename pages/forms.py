from symtable import Class

from django import forms
from produits.models import Produit

#Le formulaire python
class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit  # Définir le modèle associé
        fields = ['nom','description', 'prix']  # Spécifier les champs du formulaire

# Le formulaire django pure: l'interet ici c'est qu'on peut donner des champs encore inexistants (ici l'heritage c'est Form pas Produit)
class PurProduitFrm(forms.Form):
    nom = forms.CharField(required=True) # required=True rend le champs obligatoire dans le formulaire du coté backend car la sécurité sur le html ne suffie pas car elle peut etre enlevée
    description = forms.CharField(required=False)#
    prix = forms.FloatField()
    active = forms.BooleanField(required=False, initial=True)# On peut aussi donner valeurs par défeaut avec l'argument `initial="Nom Produit"` par exemple

