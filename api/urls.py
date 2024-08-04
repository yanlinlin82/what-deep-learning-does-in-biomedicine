from django.urls import path
from . import views

urlpatterns = [
    path('endpoint/', views.api_endpoint, name='api_endpoint'),
]
