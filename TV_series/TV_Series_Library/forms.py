from TV_Series_Library.models import Series
from django import forms

class NewSeriesForm(forms.ModelForm):
    class Meta:
        model = Series
        fields = '__all__'

class UpdateSeriesForm(NewSeriesForm):
    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        super(UpdateSeriesForm, self).__init__(*args, **kwargs)

        if instance:
            for field_name, field in self.fields.items():
                field_value = getattr(instance, field_name, '')
                field.widget.attrs['value'] = field_value
        else:
            for field_name, field in self.fields.items():
                field.widget.attrs['value'] = field_name




