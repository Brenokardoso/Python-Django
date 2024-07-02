from django.db import models
from django.contrib.auth.models import User, AbstractUser


class EnderecoUsuario(models.Model):
    rua = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    numero = models.CharField(
        max_length=10,
        null=True,
        blank=True,
    )
    cep = models.CharField(
        max_length=8,
        null=True,
        blank=True,
    )
    usuario = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
    )

    def __str__(self):
        return f"{self.usuario}"

    def save(self, *args, **kwargs):
        super().save(*args, *kwargs)
