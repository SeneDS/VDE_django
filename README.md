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
Exploration de la structure des fichiers
- management.py: 
nous permet de lancer le serveur de l'application
- requerement.txt: nous permet de stoker les versions des librairies utiliser
pip freeze > requirement.txt.
Ces deux fichiers sont en d'heors du projet (ecommerce)
- settings.py:
Ce fichier est dans le projet. C'est le fichier le plus important
- urls.py:
à chaque fois que l'on change quelque chose dans notre  base de donnée il faut executer la comande `python manage.py makermigrations`puis `python manage.py migrate`.
Je peux creer un superultilisateur `python manage.py createsuperuser`
### 1. creation de notre premiere application ou compsant avec `python manage.py startapp produits`
cette commande cree un dossier products qui a cette structure:
├── __init__.py\
├── admin.py\
├── apps.py\
├── migrations\
│   └── __init__.py\
├── models.py\
├── tests.py\
└── views.py\
Apres l'ajout de 'produit' dans le bloc 'INSTALLED_APPS' du fichier settings.py
Nous nous interessons au fichier models.py de l'applicaton produits. 
C'est là ou on créé les models de l'application, c'est à dire les tables de l'application.
#ici on crée la table Produit qui a pour chants: nom, description et prix. Cette table herite de la calsse modele.
#Pour faire apparettre cete table dans l'interface admin il faut faire la migration
```python
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
    

"""
#NB:  
blanck est par défeaut blank=False, noircie le nom du champ
default=False pour les boleens donne False comme valeur par défaut False

"""
```
NB: Les fichiers de migration generés dans le dossier migration constituent **l'historique de migration**
Ensuite, il faut enregister le modele dans le fichier qui permet d'afficher les tables: c'est le fichier admin.py
Nous allons donc importer models dans admin qui est dans le meme dossier produits.


le code est le suivante

```python
from django.contrib import admin
from .models import Produit

# Register your models here.
admin.site.register(Produit) # On enregistre la table Produit
```
Une fois cela fait, on a l'application produit et la table produit.

![shell](/Users/etienne/Documents/VDE Python/udemy_django/VDE_dango/produits/img.png)

```python
#On peux faire des enregistrements depuis le terminal
python manage.py shell
from produits.models import Produit
Produit.objects.create(nom='nouveau 3', description='nouveau 3', prix = '30')
Produit.objects.create(nom='nouveau 3', description='nouveau 3], prix = '30')

#Afficher la liste de tous les produits
Produit.objects.all()
#ffecter à une variable
produit=Produit.objects.all()
```

Apres toutes modification dans le fichier models.py, il faut generer un fichier de synchronisation avec `python manage.py makermigrations` puis synchroniser `python manage.py migrate` pour propager les modifications aux données précédentes.

### Personnalisation de la page d'accueil 
requette et réponse:

On commance par creer un app pages avec `django-admin startapp pages` que l'on refference dans le bloc INSTALLED_APPS settings.py du projet ecommerce.

Puis creer une fonction dans le fichier views.py de l'app (dossier) pages.
- Premiere vue dans vuews.py
```python
from django.shortcuts import render
from django.http import HttpResponse

def heme_view(request, *args, **kwargs):
    print(request.user)
    return HttpResponse("<h1>hello world</h1>")
```
- Son refferencement dans urls.py
```python
from pages.views import heme_view
urlpatterns = [
path('home', heme_view, name='home'),
]
```

### Django templates
On va changer: aulieu de retourner une HttpResponse, on va utiliser render qui renvoie un fichier html

```python
def heme_view(request, *args, **kwargs):
    print(request.user)
    return render(request, 'heme.html')
```
le **heme.html** que renvoie la fonction est un fichier que nous avons créer dans un dossier **templates** qui est au meme niveau que les composants du projet.
Nous avons ensuite refferencé le dossier templates dans le bloc template du fichier settings.py:  `  'DIRS': [os.path.join(BASE_DIR, 'templates')],`.
On peut également afficher le nom de l'utilisateur connecté sur la page avec cette ligne dans les templates ```<h2>{{request.user}}</h2>```.

### Les bases du template Django
Pour éviter la répétition de code dans les différents templates, il est preferable de creer un fichier **base.html** dans le dossier templates. 
Dans ce fichier nous on mettra le code partagé par les differentes pages. Puis on rajoute un block que l'on partage entre les diffrenetes pages.
```html
{% block content %}
{% endblock content %}
```
Ce block sera copier dans chaque page et un code spécifique à la page y sera mis. Par exemple
```html
{% extends 'base.html' %}

{% block content %}
<h1>Page apropos</h1>
{% endblock content %}
```
La ligne ```{% extends 'base.html' %}``` que vous voyez en haut, copie le contenu du base.html dans la page courante.
Le code dans ```base.html``` est écrite une seule fois mais il est present dans toutes les pages.
Pour les titres des pages on a le bout de code suivant dans ```base.html```
```html
    <title>{% block title %}{% endblock title %}</title>
```
Ce code est étendu aux autres pages. Par exemple dans ```home.html```
```html
{% block title %}home{% endblock title %}
```

### Template include
dans la partie precedante, nous avons vue l'heratage avec **extends**.
Dans cette partie, nous allons voir comment inclure certains bouts de code dans des fichiers html avec le template.
En effet, il peut y arriver que certaines pages n'aient pas besoin de certains bouts de code.
Dans ce cas, il faut couper ces bouts de code depuis le fichier **base.html** et les mettre dans un autre fichier. Par ici par exemple, nous avons prie le block **nav** et on l'a mis dans un ficher ```navbar.html```
Ainsi on peut choisir dans quelles pages l'inclure. Ici on peut donner l'exemple avec la page home:
```html
{% block content %}
{% include 'navbar.html' %}

<h1>Page principale</h1>
{% endblock content %}
```
Cette methode include permet également reduire le nombre de lignes de codes dans un fichier en mettant dans des fichiers séparés que l'on va inclure dans le fichier principal.
par exemple on a plusieurs sections dans home du coup pur rendre le code lisible, on la copier toutes les sections et on les a coller dans un fichier `section_home.html` que nous avons créé.
```html
<section>
    <h2>Une première section</h2>
    <p>Ceic est une première section du site</p>
</section>

<section>
    <h2>Une seconde section</h2>
    <p>Ceici est une seconde section de mon site</p>
</section>

<section>
    <h2>Une troisième section</h2>
    <p>Ceici est une troisième section de mon site</p>
</section>
```
Puis on est retourné dans `home.html` pour l'inclure avec le code suivant :
```html
{%include 'section_home.html'%}
```
**NB: l'extension peut aller sur plusieurs pages et l'inclusion peut aller sur quelques pages.**

### Les templates contexte
Ici on va parler des variables de contexte.C'est à dire des variables qui viennent du coté python vers le template.

dans le render des fonctions pythons qui sont dans le fichier views.py, on peut donner la request, le template et le contexte.
Par exemple, on peut vouloir afficher des données du backend, ici on veut afficher une liste de chiffre dans le home page:
```python
def heme_view(request, *args, **kwargs):
    print(request.user)
    list=[1, 2, 3]
    return render(request, 'home.html', {"list_1": list} )
```
Apres avoir saisi ce code dans le ficher `views.py` on peut ensuite aller visualiser le rendu depuis `home.html` comme variable de contexte dans:`{{}}`
```python
{{list_1}}
```
NB: Le bakend gerer la logique et le frontednd répond
Par exemple on ce code qui retourne le nom d'utilisateur s'il est connecté et liste liste de chiffres dans un dictionnaire que l'on affiche les valuers dans le frontend:
```python
def heme_view(request, *args, **kwargs):
    print(request.user)
    user=request.user
    list = [1, 2, 3]

    context ={
        "liste_1":list
    }
    if user.is_authenticated:
        context['user']=user.username
    else:
        context['user']='user pas connecté'
    return render(request, 'home.html', context)
```
Le résultat de ce code est capturé dans le home page grace à ce code:
ici la liste est centrée
```html
<center>{{liste_1}}</center>

{{user}}
```

### Boucles et conditions dans le template
S'il y'a plusieurs conditions à faire il est preferable de le faire dans le backend plutot que dans le frontend.
Exemple de code sur home.html
```html
{% extends 'base.html' %}

{% block title %}home{% endblock title %}

{% block content %}
{% include 'navbar.html' %}

<h1>Page principale</h1>
{% if liste_1 %}
<center>
    {% for element in liste_1  %}
    <li>
        {{element}}
    </li>
    {%empty%}
    {% endfor %}
</center>
<li>liste vide </li>
{%endif%}
    {% if request.user.is_authenticated%}
        <h1>hello {{request.user.username}}</h1>
    {% else %}
       <h1>hello guest</h1>
    {% endif %}


{%include 'section_home.html'%}
{% endblock content %}
```
### Tags dans les template (filtre)
Quand on parle de filtre c'est modifier les données qui viennent du backend mais du coté frontend (depuis les templates).
Par exemple, on peut ajouter 100 à chaque nombre de la liste.On peut également mettre la premiere lettre du titre en capital. On peut afficher la date et l'heure actuelle. Ces ajouts ne sont que du coté frontend.
NB: On a plus d'informations dans la documentation Django filter tag template.
```html
<h3>{{ liste_nombre }}</h3>
{% for nb in liste_nombre %}
<li> {{ nb|add:100 }} </li>
{% endfor %}

<h1>{% now "jS F Y H:i"%}</h1>

<h3>{{ title|capfirst }}</h3>
```

### Afficher les données venant de la bd sur le template

On créée d'abord une fonction dans le fichier views.py apres avoir importer. La fonction Produit depuis le fichier models.py du dossier produit.
Cette fonction retourne le datafram Produit_df au format html qui est dans contexte.
Et le template detail.html qui est dans un dossier templates situé dans le dossier produit.
```python
from produits.models import Produit

def product_detail_view(request):
    obj=Produit.objects.get(id=2)
    Product_df = pd.DataFrame(Produit.objects.all().values())
    #print(Product_df)
    context ={
        'obj':obj,
        'Product_df':Product_df.to_html(),
    }
    return render(request, 'produit/detail.html', context)
```
Le resultat est ensuite lié au template detail.html via ce bout de code:
```html
<div>{{Product_df|safe}}</div>
```
### Template laoder et include
Ces conceptes permettent de reutiliser un compossant ou une application dans django. Ajoutons un dossier templates dans le dossier pages.
Ensuite, on peut couper les urls qui sont dans urls.py qui est dans le dossier ecommerce pour pour les coller dans le urls.py que nous venous de crerer dans le dossier pages.

Il faut ensuite retourner dans les urls qui sont dans ecommerce en mettre en lien le nouveau fichier urls.
- On renseigne les urls dans `VDE_dango/pages/urls.py`
```python
from django.urls import path

from pages.views import heme_view, about_view, contact_view, product_detail_view
#from pages.views import *

urlpatterns = [
    path('home/',  heme_view, name='home'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('product_detail/',product_detail_view, name= "product_detail"),
    ]
```
Qu'on a coupé de `/VDE_dango/ecommerce/urls.py`
```python

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("pages.urls")),
```
On peut déplacer le dossier produit, actuellement situé dans `VDE_dango/templates/produit`, vers le dossier `templates` de l’application `pages`, sans impacter la page detail.

#### **Bonne structuration du projet :**

+ Chaque application doit contenir un dossier templates pour stocker ses fichiers HTML.
+ Chaque application doit avoir un fichier urls.py qui gère ses routes (les liens vers les vues, code python appliqué au backend).
+ Ce fichier urls.py doit être référencé dans le urls.py principal du projet avec include(), comme ceci :
`path('', include("pages.urls"))`
processus
template(html)<== urls <== Vue

### Filtres personnalisés
c'est dans cours
## 7. Formulaires
#### Moduls formulaires
Ici nous creons un formulaire permettant d'inserer des informations dans la base de données
Nous creons un fichier `forms.py`dans l'application `pages`. et un fichier `create.html`dans le dossier `produit` qui est dans template.
dans le template `create.html`
```html
{% extends 'base.html' %}

{% block title%} create block {% endblock %}

{% block content %}
    <h1 style="color: green;">{{message}}</h1>
        <form method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <input type="submit" value="Create Product">
        </form>
{% endblock %}
```
dans ce code, la 
- method="post" → Envoie les données au serveur (soumission de formulaire).
- {% csrf_token %} → Protection contre les attaques CSRF en Django.
- {{ form.as_p }} → Affiche un formulaire Django sous forme de paragraphes (<p>).
- {{ message }} Affiche un message dynamique que genere la viuws.py.
- Bouton Create Product → Permet de soumettre le formulaire.
Le backend de ce formulaire est géré par le code suivant qui est dans `views.py`

```python
from .forms import ProduitForm
def produit_create_view(request):
    form = ProduitForm(request.POST or None)
    message =''
    if form.is_valid():
        form.save()
        message= 'le produit a été bien enregistré'
        form = ProduitForm()

    context = {
        'form': form,
        'message': message,
    }
    return render(request, 'produit/create.html', context)
```
🚀 Flux de l'utilisateur\
L'utilisateur visite` /produit/create/` → Il voit un formulaire.
Il remplit le formulaire et clique sur "Créer".\
Si le formulaire est valide :
- Le produit est enregistré en base de données.
- Un message "Le produit a été bien enregistré" s'affiche.
- Un nouveau formulaire vide est affiché.
Cette fonction est reffencée dans les urls.
Ensuite 
```python
from django import forms
from produits.models import Produit

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit  # Définir le modèle associé
        fields = ['nom','description', 'prix']  # Spécifier les champs du formulaire

```
Nous avons ensuite créé un ficher `forms.py`pour dont le code définit un formulaire Django basé sur le modèle Produit. 
Son code est utilisé pour créer ou modifier un produit via un formulaire HTML.
```
✅ Crée un formulaire Django basé sur le modèle Produit.
✅ Génère automatiquement les champs nom, description et prix.
✅ Simplifie l’enregistrement d’un produit sans écrire manuellement un formulaire HTML.
```