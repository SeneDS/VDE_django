from lib2to3.fixes.fix_input import context
import pandas as pd

from django.shortcuts import render
from django.http import HttpResponse
from produits.models import Produit
from .forms import *


def product_detail_view(request):
    obj=Produit.objects.get(id=2)
    Product_df = pd.DataFrame(Produit.objects.all().values())
    #print(Product_df)
    context ={
        'obj':obj,
        'Product_df':Product_df.to_html(),
    }
    return render(request, 'produit/detail.html', context)



def heme_view(request, *args, **kwargs):
    print(request.user)
    user=request.user
    list = [1, 2, 3]

    context ={
        "liste_1":list,
        "user":user
    }
    return render(request, 'home.html', context)



def about_view(request, *args, **kwargs):
    print(request.user)
    liste_nombre=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    context = {"liste_nombre" :  liste_nombre,
               "title":"About as",
               "MyNumber": 123,}
    return render(request, 'about.html',  context)

def contact_view(request, *args, **kwargs):
    print(request.user)
    return render(request, 'contact.html')

# Create your views here.
"""
from .forms import ProduitForm
def produit_create_view(request):
    message = ''
    if request.method == 'POST':
        data = request.POST
        nom = data.get("nom")
        prix = data.get("prix")
        description = data.get("description")
        Produit.objects.create(nom=nom, prix=prix, description=description)

        message = 'produit a été bien enregistré avec succès'

    return render(request, 'produit/create.html', {'message':message})
"""
"""
from .forms import ProduitForm, PurProduitFrm
def produit_create_view(request, *args, **kwargs):
    message=''
    form = PurProduitFrm(request.POST or None)
    if form.is_valid():
        form.save()
        message = "données enregistrées"

    return render(request, 'produit/create.html', {'message':message, 'form': form})
"""


from django.shortcuts import render
from .forms import PurProduitFrm  # Import du formulaire
from produits.models import Produit  # Import du modèle

def produit_create_view(request):
    message = '' # Initialisation du message
    form = PurProduitFrm(request.POST or None) # Création du formulaire

    if request.method == 'POST':
        if form.is_valid():
### début de bloc de validation##########################################################
            nom = form.cleaned_data['nom']
            description = form.cleaned_data['description']
            if nom != 'ES':
                message =f'❌ Le nom du produit  doit être "ES"'
### Fin de bloc ##########################################################
            else:
                Produit.objects.create(**form.cleaned_data) # Enregistre en base les ** c'est pour exploser le dictionnaire et si c'est une liste il suffit de mettre une seule étoile *
                message = '✅ Produit enregistré avec succès !'  # Met à jour le message
                form = PurProduitFrm()  # Réinitialise le formulaire uniquement si la création a réussi

    return render(request, 'produit/create.html', {'form': form, 'message': message})


