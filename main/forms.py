from django import forms
from .models import Reja
class RejaForm(forms.ModelForm):
    class Meta:
        model=Reja
        fields=('sarlavha','batafsil','sana','bajarildi','student')
