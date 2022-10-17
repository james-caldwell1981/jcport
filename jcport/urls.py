from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing, name='landing'),
    path('contact/', views.contact, name='contact')
]
