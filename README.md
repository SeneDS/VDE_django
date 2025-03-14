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