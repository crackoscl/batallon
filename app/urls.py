
from django.urls import path
from .views import ListClubes, ListPeleadores,RatingList, get_comuna, DetallePelador, DetalleClub

app_name = "app"

urlpatterns = [
    path('',ListClubes.as_view(),name='principal'),
    path('peleadores/',ListPeleadores.as_view(),name='peleadores'),
    path('rating/<int:pk>/',RatingList.as_view(),name='rating'),
    path('get_comuna/',get_comuna,name='comuna'),
    path('detalle/<int:pk>', DetallePelador.as_view(),name='detalle_peleador'),
    path('detalle/<int:pk>', DetalleClub.as_view(),name='detalle_club')
]