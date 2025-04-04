from django.urls import path
from . import api_views

from django.urls import path
from . import api_views

urlpatterns = [
    path('', api_views.api_product_list, name='api_product_list'),
    path('create/', api_views.api_product_create, name='api_product_create'),
    path('<int:pk>/', api_views.api_product_detail, name='api_product_detail'),
    path('<int:pk>/update/', api_views.api_product_update, name='api_product_update'),
    path('<int:pk>/delete/', api_views.api_product_delete, name='api_product_delete'),
]

