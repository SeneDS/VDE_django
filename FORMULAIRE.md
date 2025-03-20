
# VDE_django

### Objectif du cours Udemy:
Nous allons commencer par les bases fondamentales et progresser graduellement
vers des concepts plus avancés.
Pas à pas, nous allons explorer de nouvelles fonctionnalités et techniques.
Tout en réalisant des projets qui vous permettront d'acquérir une autonomie à
l'utilisation de ce framework.
Acquérir énormément de compétences et comprendre comment le framework fonctionne.

### Projet:

Développer une application de eCommerce intégrant les API de paiement.
Ensuite, nous allons développer une application de facturation.
Qui permet de générer des reçus au format PDF.
Et enfin, nous allons voir comment créer une application ou développer une application qui génère les
QR codes selon les URL ou les textes entrés par un utilisateur.






## Notes:
### HTML formulaires

### HTML formulaires
Comment developper nos formulaires avec le HTML et les recuperer avec django ?
Precedament nous avons utilisé django forms pour générer nos formulaire.
Nous avons sécurisé les données avec le `csrf_token`
Pour ce faire j'ai modifié le code html du template `create.html`

```html
{% extends 'base.html' %}

{% block title %} Create Product {% endblock %}

{% block content %}
    <h1>Welcome to the create product page</h1>

    {% if message %}
        <h2 style="color: green;">{{ message }}</h2>
    {% endif %}

    <form method="post" action=".">
        {% csrf_token %}

        <label for="nom">Nom du produit :</label><br>
        <input type="text" id="nom" name="nom" placeholder="Nom du produit" required><br><br>

        <label for="prix">Prix du produit :</label><br>
        <input type="number" id="prix" name="prix" placeholder="Prix du produit" required><br><br>

        <label for="description">Description :</label><br>
        <textarea id="description" name="description" cols="30" rows="10" placeholder="Description du produit" required></textarea><br><br>

        <input type="submit" value="Envoyer">
    </form>
{% endblock %}
```

Explications:
- Ce template hérite d'un fichier base.html qui contient la structure de base du site (header, footer, styles CSS, etc.).
- Il permet de réutiliser une mise en page commune à plusieurs pages.
- Définit le titre de la page ``(<title>`` dans base.html).
- ```{% block title %}...{% endblock %}``` permet d’insérer un contenu dans le <title> de base.html.
- Tout le contenu entre ```{% block content %} ... {% endblock %}``` est inséré à l'endroit où base.html définit {% block content %}.
- ```{{ message }}``` : Variable envoyée par Django depuis la vue (produit_create_view).
- Elle affiche un message (ex : "Produit enregistré avec succès").
- Si aucun message n'est défini, rien ne s’affiche.
- method="post" : Envoie les données en POST (utilisé pour modifier la base de données).
- ```action="." ```: Envoie le formulaire à la même URL que la page actuelle.
- ```{% csrf_token %}``` : Sécurise le formulaire avec un jeton CSRF pour éviter les attaques CSRF.
- name="nom" : Correspond à ```request.POST["nom"]``` dans la vue Django.
- name="prix" : Correspond à ```request.POST["prix"]``` (⚠️ erreur, type="int" n'existe pas, il faut mettre type="number").
- name="description" : Définit la description du produit.
- Envoie les données du formulaire à la vue Django (produit_create_view).

J'ai également modifié la fonction de la vue:\

```python
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
```
Explication:
- Cette vue est basée sur une fonction (FBV - Function-Based View) qui gère l'affichage et la soumission d'un formulaire.
- On initialise une variable message qui servira à afficher une confirmation à l'utilisateur après l'enregistrement du produit.
- On Vérifie si le formulaire a été soumis en POST (ce qui signifie que l'utilisateur a cliqué sur "Soumettre").
- request.POST contient toutes les données envoyées par le formulaire.
- .get("nom") récupère la valeur du champ nom sans provoquer d'erreur si le champ est absent.
-Produit est un modèle Django, qui est défini dans models.py.
- objects.create(...) crée et enregistre directement un nouvel objet en base de données.
- Une fois le produit créé, on met à jour message pour informer l'utilisateur que l'opération a réussi.
- La derniere ligne retourne la page create.html dans le dossier produit/, en envoyant le message à afficher dans le template.

### Pure Django formulaire (formulaire django pure)
J'ai modifié le code qui est dans forms. Le formulaire django pure utilisé ici permet de donner des champs encore inexistants (ici l'heritage c'est Form pas Produit). Par exemple je peux ajouter le champ ``` active = forms.BooleanField(required=False)```sans erreur.
On peut aussi donner valeurs par défeaut avec l'argument `initial="Nom Produit"` par exemple
```python 
from django import forms
class PurProduitFrm(forms.Form):
    nom = forms.CharField(required=True) # required=True rend le champs obligatoire dans le formulaire du coté backend car la sécurité sur le html ne suffie pas car elle peut etre enlevée
    description = forms.CharField(required=False)#
    prix = forms.FloatField()
    active = forms.BooleanField(required=False, initial=True)
```

Je modifie ensuite le code dans la vue: en gros, je recupere les données du formulaire `form = ProduitForm(request.POST or None)` s'il y en a que j'enregistre si elles sont valides.
J'envoie ensuite un message de confirmation

```python

from django.shortcuts import render
from .forms import PurProduitFrm  # Import du formulaire
from produits.models import Produit  # Import du modèle

def produit_create_view(request):
    message = ''  # Initialisation du message
    form = PurProduitFrm(request.POST or None)  # Création du formulaire

    if request.method == 'POST':
        if form.is_valid():  # Vérifie si le formulaire est valide
            Produit.objects.create(**form.cleaned_data)  # Enregistre en base les ** c'est pour exploser le dictionnaire et si c'est une liste il suffit de mettre une seule étoile *
            message = '✅ Produit enregistré avec succès !'  # Met à jour le message

            # Réinitialiser le formulaire après soumission
            form = PurProduitFrm()

    return render(request, 'produit/create.html', {'form': form, 'message': message})
```
Je vais ensuite récuperer le formulaire via `create.html`

```html
{% extends 'base.html' %}

{% block title %} Create Product {% endblock %}

{% block content %}
    <h1>Welcome to the create product page</h1>

    {% if message %}
        <h2 style="color: green;">{{ message }}</h2>
    {% endif %}

    <form method="post" action=".">
        {% csrf_token %}
        {{form.as_p}}
        <input type="submit" value="Envoyer">
    </form>
{% endblock %}
```
la methode `as_p` renvoie le formulaire en paragraph, la methode `as_ul` le renvoie en liste.

