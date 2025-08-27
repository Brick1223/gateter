from django.contrib import admin
from .models import Meow  # Importa el modelo Meow desde la app actual

# =========================
# Registro del modelo Meow en el panel de administración
# =========================
@admin.register(Meow)
class MeowAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista de objetos
    list_display = ('author', 'body', 'created_at')
    
    # Campos que se podrán buscar en la barra de búsqueda del admin
    search_fields = ('body', 'author__username')
    
    # Filtros laterales en el admin para facilitar la búsqueda por fecha
    list_filter = ('created_at',)
