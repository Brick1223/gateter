from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),                     # http://127.0.0.1:8000/
    path('registro/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('usuarios/<str:username>/', views.profile_view, name='profile'),
    path('buscar-usuarios/', views.user_search_view, name='user_search'),  # Nueva ruta para búsqueda de usuarios
]
