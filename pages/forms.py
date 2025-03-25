from django import forms
from produits.models import Produit

# Formulaire basé sur le modèle
class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['nom', 'description', 'prix']


# Formulaire non lié à un modèle (formulaire pur Django)
class PurProduitFrm(forms.Form):
    nom = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'name',
                'placeholder': 'Entrez le nom du produit'
            }
        )
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "rows": 5,
                "cols": 20,
                "class": "desc",  # 'classe' corrigé en 'class'
                "id": "description",
                "placeholder": "Entrez la description du produit"
            }
        )
    )
    prix = forms.FloatField(
        required=False,
        initial=12.6,
        label="Prix du produit"
    )
    active = forms.BooleanField(
        required=False,
        initial=True,
        help_text="Ce champ indique si le produit est actif ou non"
    )
