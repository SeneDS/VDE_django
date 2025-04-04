

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect





from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('api_product_list')),  # ou 'home' si tu as une page d’accueil HTML
    path('api/produits/', include('produits.urls_api')),     # si ton fichier api s'appelle urls_api.py
]
