from django import forms
from frames.models import Optical
class NewForm(forms.ModelForm):
      class Meta:
          model = Optical
          fields ='__all__'
