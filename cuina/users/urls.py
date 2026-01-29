from django.urls import path
from .views import preview_base, login, register, error

urlpatterns = [
    path("preview/", preview_base, name="preview_base"),
    path("login/", login, name="login"),
    path("register/", register, name="register"),
    path("error/", error, name="error"),
]
