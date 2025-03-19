from django.urls import path

from pages.views import heme_view, about_view, contact_view, product_detail_view
#from pages.views import *

urlpatterns = [
    path('home/',  heme_view, name='home'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('product_detail/',product_detail_view, name= "product_detail"),
    ]