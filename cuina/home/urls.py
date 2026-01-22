from django.urls import path
from .views import preview_base

urlpatterns = [
    path("preview/", preview_base, name="preview_base"),
]
