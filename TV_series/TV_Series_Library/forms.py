from TV_Series_Library.models import Series
from django import forms

class SeriesForm(forms.ModelForm):
    class Meta:
        model = Series
        fields = '__all__'






