from django import forms
from . import models

class ChoiceGameForm(forms.Form):
    choice = forms.ChoiceField(choices=[('C', 'Coin'), ('D', 'Dice'), ('H', 'Hundred')])
    count = forms.IntegerField(min_value=1, max_value=64, widget=forms.NumberInput(attrs={'class': 'form-control'}))
