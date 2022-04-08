from django.shortcuts import render

from django.shortcuts import render
from django.views import View

from scraping.models import Vacancy
from scraping.forms import SearchForm


class HomeView(View):
    def get(self, request):
        form = SearchForm(request.GET)
        city = request.GET.get('city')
        programming_language = request.GET.get('programming_language')
        _filter = {}
        if city or programming_language:
            if city:
                _filter['city__slug'] = city
            if programming_language:
                _filter['programming_language__slug'] = programming_language
        vacancies = Vacancy.objects.filter(**_filter)
        context = {'vacancies': vacancies, 'form': form}
        return render(request, 'scraping/home.html', context)
