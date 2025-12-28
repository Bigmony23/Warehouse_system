from django.urls import path

from inventory.views import PostProductsView

urlpatterns=[
    path('inventory/',PostProductsView.as_view(),name='inventory'),
]