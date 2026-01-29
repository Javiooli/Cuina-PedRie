from django.urls import path
from .views import faqs, error

urlpatterns = [
    path("", faqs, name="faqs"),
    path("error/", error, name="error"),
]
