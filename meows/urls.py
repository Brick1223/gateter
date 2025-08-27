from django.urls import path
from . import views

# =========================
# Rutas de la aplicación Gateter
# =========================
urlpatterns = [
    path('', views.home_view, name='home'),                     # Página principal / inicio
    path('registro/', views.register_view, name='register'),    # Página de registro de usuario
    path('login/', views.login_view, name='login'),             # Página de inicio de sesión
    path('logout/', views.logout_view, name='logout'),          # Cierre de sesión
    path('usuarios/<str:username>/', views.profile_view, name='profile'),  # Perfil de usuario por username
    path('buscar-usuarios/', views.user_search_view, name='user_search'),  # Búsqueda de usuarios
]
