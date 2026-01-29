from django.urls import path
from .views import enter_recipes, error

urlpatterns = [
    path("", enter_recipes, name="enter_recipes"),
    path("error/", error, name="error"),
]
