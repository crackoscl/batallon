
from django.urls import path
from .views import ListClubes, ListPeleadores,Rating_list, get_comuna

app_name = "app"

urlpatterns = [
    path('',ListClubes.as_view(),name='principal'),
    path('peleadores/',ListPeleadores.as_view(),name='peleadores'),
    path('rating/<int:pk>/',Rating_list.as_view(),name='rating'),
    path('get_comuna/',get_comuna,name='comuna')
]