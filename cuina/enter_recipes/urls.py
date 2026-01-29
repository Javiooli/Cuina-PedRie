from django.urls import path
from .views import preview_base, enter_recipes, error

urlpatterns = [
    path("preview/", preview_base, name="preview_base"),
    path("", enter_recipes, name="enter_recipes"),
    path("error/", error, name="error"),
]
