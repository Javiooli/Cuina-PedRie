from django.urls import path
from .views import admin_requests, error

urlpatterns = [
    path("", admin_requests, name="admin_requests"),
    path("error/", error, name="error"),
]
