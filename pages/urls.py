from django.core.management.commands.runserver import naiveip_re
from django.urls import path

from pages.views import heme_view, about_view, contact_view, product_detail_view, produit_create_view, product_delete_view, product_list_view

#from pages.views import *

urlpatterns = [
    path('home/',  heme_view, name='home'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('product_detail/<int:my_id>/',product_detail_view, name= "product_detail"),
    path('create/', produit_create_view, name="create"),
    path('product_delete/<int:my_id>/', product_delete_view, name='product_delete'),
    path('product_list', product_list_view, name='product_list'),

    ]

