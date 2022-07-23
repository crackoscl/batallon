from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .resources import RatingResource
from .models import Clubes, Peleador, Categorias , Rating,Region, Comuna,Eventos
from .forms import ClubForm



class ClubesAdmin(admin.ModelAdmin):
    form = ClubForm


class RatingAdmin(ImportExportModelAdmin):
    resource_class = RatingResource


    

admin.site.register(Peleador)
admin.site.register(Rating,RatingAdmin)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Categorias)
admin.site.register(Eventos)
admin.site.register(Clubes,ClubesAdmin)