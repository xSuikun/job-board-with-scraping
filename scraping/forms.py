from django import forms

from scraping.models import City, ProgrammingLanguage


class SearchForm(forms.Form):
    city = forms.ModelChoiceField(
        queryset=City.objects.all(), required=False, to_field_name='slug',
        widget=forms.Select(attrs={'class': 'form-control'}), label='Город')
    programming_language = forms.ModelChoiceField(
        queryset=ProgrammingLanguage.objects.all(), required=False, to_field_name='slug',
        widget=forms.Select(attrs={'class': 'form-control'}), label='Город')

