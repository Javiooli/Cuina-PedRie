from django.urls import path
from .views import preview_base, home

urlpatterns = [
    path("preview/", preview_base, name="preview_base"),
    path("home/", home, name="home")
]
