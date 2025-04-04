from django.core.management.commands.runserver import naiveip_re
from django.urls import path

from pages.views import heme_view, about_view, contact_view, product_detail_view, produit_create_view, product_delete_view, product_list_view, product_update_view

#from pages.views import *


from django.urls import path
from pages.views import (
    heme_view,
    about_view,
    contact_view,
    product_detail_view,
    produit_create_view,
    product_delete_view,
    product_list_view,
    product_update_view,
)

urlpatterns = [
    path('home/', heme_view, name='home'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),

    # CRUD Produits
    path('produits/', product_list_view, name='product_list'),
    path('produits/create/', produit_create_view, name='create'),
    path('produits/<int:my_id>/', product_detail_view, name='product_detail'),
    path('produits/<int:my_id>/modifier/', product_update_view, name='product_update'),
    path('produits/<int:my_id>/supprimer/', product_delete_view, name='product_delete'),
]
