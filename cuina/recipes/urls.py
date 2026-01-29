from django.urls import path
from .views import preview_base, recipes, error

urlpatterns = [
    path("preview/", preview_base, name="preview_base"),
    path("", recipes, name="recipes"),
    path("error/", error, name="error"),
]
