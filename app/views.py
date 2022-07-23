from django.shortcuts import render, HttpResponse
from django.views import View
from django.views.generic import ListView,DetailView
from django.contrib.auth.decorators import user_passes_test,login_required
import json
from .models import Clubes, Peleador,Rating, Comuna,Eventos

# Create your views here.


class Eventos(ListView):
    model = Eventos
    template_name = 'app/eventos.html'
    context_object_name = 'lista_eventos'
    


class ListClubes(ListView):
    model = Clubes
    template_name = 'app/index.html'
    context_object_name = 'lista_clubes'

  

class ListPeleadores(ListView):
    model = Peleador
    template_name = 'app/peleadores.html'
    context_object_name = 'lista_peleadores'




class RatingList(View):
    def get(self,request,pk):
        rating = Rating.objects.filter(categoria=pk)
        return render(request,'app/rating.html',{'lista_rating':rating})


class DetallePelador(DetailView):
    template_name = 'app/ficha_peleador.html'
    model = Peleador
    context_object_name = "detalle"

    def get_context_data(self, **kwargs):
        context = super(DetallePelador, self).get_context_data(**kwargs) # default
        context['ranking'] = Rating.objects.filter(peleador_id=self.object)
        return context


class DetalleClub(DetailView):
    template_name = 'app/ficha_club.html'
    model = Clubes
    context_object_name = "detalle"

    def get_context_data(self, **kwargs):
        context = super(DetalleClub, self).get_context_data(**kwargs) # default
        context['peleadores'] = Peleador.objects.filter(club_id=self.object)
        return context


    
@user_passes_test(lambda u: u.is_superuser)
@login_required
def get_comuna(request):
    id = request.GET.get('id','')
    print('aqui',request.GET)
    result = list(Comuna.objects.filter(region_id=int(id)).values('id','nombre'))
    return HttpResponse(json.dumps(result), content_type="application/json")



    

