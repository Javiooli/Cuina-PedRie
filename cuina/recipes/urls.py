from django.urls import path
from .views import recipes, error

urlpatterns = [
    path("", recipes, name="recipes"),
    path("error/", error, name="error"),
]
