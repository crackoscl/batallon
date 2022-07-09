from django import forms
from .models import Clubes


class ClubForm(forms.ModelForm):
    model = Clubes
    class Meta:
        fields = '__all__'
    class Media:
        js = ('js/main.js',)



