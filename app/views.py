
from django.shortcuts import render, HttpResponse
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.decorators import user_passes_test,login_required
import json
from .models import Clubes, Peleador, Categorias, Rating, Comuna, Region

# Create your views here.
class ListClubes(ListView):
    model = Clubes
    template_name = 'app/index.html'
    context_object_name = 'lista_clubes'

    def get_context_data(self, **kwargs):
        context = super(ListClubes, self).get_context_data(**kwargs) # default
        context['categorias'] = Categorias.objects.all()
        return context


class ListPeleadores(ListView):
    model = Peleador
    template_name = 'app/peleadores.html'
    context_object_name = 'lista_peleadores'

    def get_context_data(self, **kwargs):
        context = super(ListPeleadores, self).get_context_data(**kwargs) # default
        context['categorias'] = Categorias.objects.all()
        return context


class Rating_list(View):
    def get(self,request,pk):
        categorias = Categorias.objects.all()
        rating = Rating.objects.filter(categoria=pk)
        return render(request,'app/rating.html',{'lista_rating':rating,'categorias': categorias})
        
    
@user_passes_test(lambda u: u.is_superuser)
@login_required
def get_comuna(request):
    id = request.GET.get('id','')
    print('aqui',request.GET)
    result = list(Comuna.objects.filter(region_id=int(id)).values('id','nombre'))
    return HttpResponse(json.dumps(result), content_type="application/json")





    

