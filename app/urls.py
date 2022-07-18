
from django.urls import path
from .views import ListClubes, ListPeleadores,RatingList, get_comuna, DetallePelador, DetalleClub,Eventos

app_name = "app"

urlpatterns = [
    path('',Eventos.as_view(),name='eventos'),
    path('clubes/',ListClubes.as_view(),name='principal'),
    path('peleadores/',ListPeleadores.as_view(),name='peleadores'),
    path('rating/<int:pk>/',RatingList.as_view(),name='rating'),
    path('get_comuna/',get_comuna,name='comuna'),
    path('peleador/detalle/<int:pk>', DetallePelador.as_view(),name='detalle_peleador'),
    path('club/detalle/<int:pk>', DetalleClub.as_view(),name='detalle_club')
]