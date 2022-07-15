from .models import Categorias

def list_categorias(request):
    list_categorias = Categorias.objects.all()
    return {'lista_categorias': list_categorias}