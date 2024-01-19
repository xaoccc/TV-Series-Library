from TV_Series_Library.models import Season, Episode, Series
from django import forms

class NewSeriesForm(forms.ModelForm):
    class Meta:
        model = Series
        fields = '__all__'

