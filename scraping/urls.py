from django.contrib import admin
from django.urls import path, include

from scraping.views import HomeView

urlpatterns = [
    path('work/', HomeView.as_view()),
]