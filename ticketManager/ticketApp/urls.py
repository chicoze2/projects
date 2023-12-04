from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home_url'),

    ## SUPERVISOR
    path('supervisor', views.supervisor_view, name='supervisor_url'),
    path('create-empresa', views.create_empresa_view, name='create_empresa_url'),

    ## PROTOCOL RELATED
    path('create-protocol', views.create_protocol_view, name='create_protocol_url'),
    path('edit-protocol/<str:pk>/', views.edit_protocol_view, name='edit_protocol_url'),
    
    ## USER
    path('login', views.login_view, name='login_url'),
    path('logout', views.logout_function, name='logout_url'),
    path('register', views.create_new_user_view, name='register_url'),
    path('update-user/<int:user_id>', views.update_user_view, name='update_user_url'),
    path('update-user', views.update_user_view, name='update_user_url'),


    
    ##??
    path('listby-empresa', views.list_by_empresa_view, name='list_by_empresa_url'),
]