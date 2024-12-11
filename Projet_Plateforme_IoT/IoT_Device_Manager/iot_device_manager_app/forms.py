from django import forms
from .models import Sensor, Unit

class SensorForm(forms.ModelForm):
    class Meta:
        model = Sensor
        fields = ['name', 'longi', 'lati', 'period']

class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['name']