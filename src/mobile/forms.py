from django import forms
from mobile.models import *

class MobileForm(forms.ModelForm):

    jan_code = forms.CharField()

    class Meta:
        model = Mobile
        fields = ('brand_name', 'model', 'jan_code', 'color')

    def clean_jan_code(self):
 
        jan_code =self.cleaned_data.get('jan_code')
    
        try:
            data = Mobile.objects.get(jan_code=jan_code)
            raise forms.ValidationError("Invalid Jan Code")
        except:
            return jan_code

