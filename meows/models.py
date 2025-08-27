from django.db import models
from django.conf import settings

class Meow(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='meows'
    )
    body = models.CharField(max_length=140)  # texto del maullido
    created_at = models.DateTimeField(auto_now_add=True)  # fecha de creación

    class Meta:
        ordering = ['-created_at']  # siempre del más reciente al más antiguo

    def __str__(self):
        return f"{self.author.username}: {self.body[:30]}"
