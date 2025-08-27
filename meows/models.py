from django.db import models
from django.conf import settings

# =========================
# Modelo para los maullidos (publicaciones)
# =========================
class Meow(models.Model):
    # Relación con el usuario que creó el maullido
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,  # elimina los maullidos si se elimina el usuario
        related_name='meows'      # permite acceder a los maullidos desde user.meows
    )
    body = models.CharField(max_length=140)  # texto del maullido, máximo 140 caracteres
    created_at = models.DateTimeField(auto_now_add=True)  # fecha y hora de creación automática

    class Meta:
        ordering = ['-created_at']  # ordena los maullidos del más reciente al más antiguo

    def __str__(self):
        # Representación legible del maullido (primeros 30 caracteres)
        return f"{self.author.username}: {self.body[:30]}"
