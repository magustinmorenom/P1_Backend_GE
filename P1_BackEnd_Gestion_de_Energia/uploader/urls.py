# myapi/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('getScans/', views.get_scans, name='get_scans'),
]