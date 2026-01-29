from django.urls import path
from .views import login, register, error

urlpatterns = [
    path("login/", login, name="login"),
    path("register/", register, name="register"),
    path("error/", error, name="error"),
]
