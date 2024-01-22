from TV_Series_Library.models import Season, Episode, Series
from django import forms

class NewSeriesForm(forms.ModelForm):
    class Meta:
        model = Series
        fields = '__all__'

class UpdateSeriesForm(NewSeriesForm):
    # def __init__(self, *args, **kwargs):
    #     super(UpdateSeriesForm, self).__init__(*args, **kwargs)
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs['value'] = f'Enter your new {field.label}'

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        super(UpdateSeriesForm, self).__init__(*args, **kwargs)

        if instance:
            # Set placeholders based on model instance values
            for field_name, field in self.fields.items():
                field_value = getattr(instance, field_name, '')
                field.widget.attrs['value'] = field_value




