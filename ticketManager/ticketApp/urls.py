from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home_url'),
    path('create-protocol', views.create_protocol_view, name='create_protocol_url'),
    
]