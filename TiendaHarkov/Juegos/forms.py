from django import forms

from Juegos.models import videojuegos

class VideojuegosForm(forms.ModelForm):
    name = forms.CharField(label='Titulo',max_length=200, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    pegi = forms.CharField(label='Descripción', max_length=1000, widget=forms.Textarea(
        attrs={
            'class':'form-control'
        }
    ))
    class Meta:
        model = videojuegos
        fields = ('name', 'pegi',)
