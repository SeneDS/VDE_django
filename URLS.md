
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
### URLS
#### Rootage url dynamique
Ici nous nous concentrons sur le rootage des urls de façon dynamique.
Pour ce faire, aulieu d'afficher un dataframe pour les détails, j'ai commenté le code da la vue qui renvoie le datafram et mis en place ce code qui nous renvoie les valeurs d'un objet dont l'identifianserait suivi d'un slache "/1/" sur l'url de la page details ``product_detail/1/``
```python
def product_detail_view(request, my_id):
    obj=Produit.objects.get(id=my_id)
    context ={
        'obj':obj }
    return render(request, 'produit/detail.html', context)
```
Puis j'ai modifié le path de la vue dans les urls en ajoutant cette partie ``<int:my_id>``.
```python 
path('product_detail/<int:my_id>/',product_detail_view, name= "product_detail"),
```
#### Gerer les erreures 404 de la db
Dans cette partie, j'apprend à gerer les pages introuvables. au niveau des requettes dans la base de données.
La premiere option que je choisi est des d'importer ``get_object_or_404`` depuis ``django.shortcuts`` dans views.py.
```python
def product_detail_view(request, my_id):
    #obj=Produit.objects.get(id=my_id)
    obj = get_object_or_404(Produit, pk=my_id)
    context ={
        'obj':obj }
    return render(request, 'produit/detail.html', context)
```
#### Suppression dynamique
Dans cette section j'apprend comment confiner un objet avent de le supprimer.
On import d'abord ``redirect``.
On ajoute d'abord une vue 
```python
def product_delete_view(request, my_id):
    obj = get_object_or_404(Produit, pk=my_id)
    if request.method == "POST":
        obj.delete()
        return redirect('produit/detail.html')  # Rediriger vers la page d'accueil ou autre
    return render(request, 'produit/delete.html', {'obj': obj})
```
Qu'on rajoute ensuite aux urls
```python
  path('product_delete/<int:my_id>/', product_delete_view, name='product_delete'),
```
Puis on créée un fichier ``delete.html`` dans ``templates/produit``. pour lequel on a le contenu suivant:
```html
{% extends "base.html" %}

{% block content %}
<h2> Page de suppression de produit</h2>

<p> Etes vous sure de vouloir supprimer le produit {{obj.nom}} ?</p>

<form method="POST">
   {% csrf_token %}
    <input type="submit" value="Supprimer">
</form>
{% endblock %}
```

#### Listing et Urls
Ici nous allons voir comment lister tous les produits de la base de données.
Pour ce faire, il nous faut creer une vue de listing.


