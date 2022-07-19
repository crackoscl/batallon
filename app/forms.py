from django import forms
from .models import Clubes, Comuna


class ClubForm(forms.ModelForm):
    model = Clubes
    class Meta:
        fields = '__all__'
    class Media:
        js = ('js/main.js',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comuna'].queryset = Comuna.objects.none()

        if 'region' in self.data:
            try:
                region_id = int(self.data.get('region'))
                self.fields['comuna'].queryset = Comuna.objects.filter(region_id=region_id).order_by('nombre')
            except (ValueError, TypeError):
                pass  # Entrada no valida del cliente, ignora y regresa al conjunto de consulta vacia
        elif self.instance.pk:
            self.fields['comuna'].queryset = self.instance.region.comunas.order_by('nombre')


