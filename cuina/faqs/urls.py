from django.urls import path
from .views import preview_base, faqs, error

urlpatterns = [
    path("preview/", preview_base, name="preview_base"),
    path("", faqs, name="faqs"),
    path("error/", error, name="error"),
]
