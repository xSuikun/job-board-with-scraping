import datetime

from django.shortcuts import render
from django.views import View


class HomeView(View):
    def get(self, request):
        date = datetime.datetime.now().date()
        name = 'Саня'
        context = {'date': date, 'name': name}
        return render(request, 'home.html', context)
