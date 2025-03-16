# VDE_dango

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
```
class Produit(models.Model):
    nom          = models.CharField()
    description = models.TextField()
    prix        = models.IntegerField()
#NB:  
"""
blanck est par défeaut blank=False, noircie le nom du champ
default=False pour les boleens donne False comme valeur par défaut False

"""
```
NB: Les fichiers de migration generés dans le dossier migration constituent **l'historique de migration**
Ensuite, il faut enregister le modele dans le fichier qui permet d'afficher les tables: c'est le fichier admin.py
Nous allons donc importer models dans admin qui est dans le meme dossier produits.


le code est le suivante

```
from django.contrib import admin
from .models import Produit

# Register your models here.
admin.site.register(Produit) # On enregistre la table Produit
```
Une fois cela fait, on a l'application produit et la table produit.

![shell](/Users/etienne/Documents/VDE Python/udemy_django/VDE_dango/produits/img.png)

```
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
