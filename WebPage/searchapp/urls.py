from django.urls import path
from .views import search

app_name = 'searhapp'

urlpatterns = [
	path('', search, name="search"),
]
