from django import forms
from django.forms import ModelForm
from .models import Buku

# class PostForm(forms.Form):
#     judul = forms.CharField(max_length=50)
#     penulis = forms.CharField(max_length=40)
#     penerbit = forms.CharField(max_length=40)

class FormBuku(ModelForm):
    class Meta:
        model = Buku
        fields = '__all__'

        widgets = {
            'judul' : forms.TextInput({'class':'form-control'}),
            'penulis' : forms.TextInput({'class':'form-control'}),
            'penerbit' : forms.TextInput({'class':'form-control'}),
            'jumlah_buku' : forms.NumberInput({'class':'form-control'}),
            'kelompok_id' : forms.Select({'class':'form-control'}),
        }