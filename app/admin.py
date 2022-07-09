from django.contrib import admin
from .models import Clubes, Peleador, Categorias , Rating,Region, Comuna
from .forms import ClubForm


class ClubesAdmin(admin.ModelAdmin):
    form = ClubForm



admin.site.register(Peleador)
admin.site.register(Categorias)
admin.site.register(Rating)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Clubes,ClubesAdmin)