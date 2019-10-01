from django import forms


CHOICES = (('Accuweather', 'Accuweather'),
           ('Weather.com', 'Weather.com'),
           ('NOAA', 'NOAA'),
           )


class WheatherForm(forms.Form):
    services = forms.MultipleChoiceField(
        choices=CHOICES,
        label='SELECT SERVICES:',
        widget=forms.CheckboxSelectMultiple,
        help_text='You choose at least one')
    latitud = forms.DecimalField(
        max_value=90, min_value=-90, help_text='Introduce a decimal between 90 and -90',
    )

    longitud = forms.DecimalField(
        max_value=90, min_value=-90, help_text='Introduce a decimal between 90 and -90',
    )
