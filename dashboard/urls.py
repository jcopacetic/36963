from django.urls import path

from .views import Dashboard

urlpatterns = [
    path("", Dashboard, name="dashboard"),
]
