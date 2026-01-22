from django.urls import path
from .views import preview_base, home, error

urlpatterns = [
    path("preview/", preview_base, name="preview_base"),
    path("", home, name="home"),
    path("error/", error, name="error"),
]
