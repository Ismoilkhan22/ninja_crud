from django.urls import path
from src.dninja.api import api


urlpatterns = [
    path("", api.urls)
]