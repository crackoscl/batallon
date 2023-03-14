from .models import Categorias

def list_categorias_menu(request):
    list_categorias = Categorias.objects.all()
    return {'lista_categorias': list_categorias}