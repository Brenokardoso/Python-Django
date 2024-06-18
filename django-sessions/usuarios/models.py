from django.db import models


class Usuario(models.Model):
    nome = models.CharField(
        verbose_name="Nome",
        max_length=100,
        null=True,
        blank=True,
    )
    email = models.EmailField(
        verbose_name="Email",
        max_length=250,
        null=True,
        blank=True,
    )
    senha = models.CharField(
        verbose_name="Email",
        max_length=64,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.nome}-{self.email}"

    class Meta:
        ordering = ["nome"]

    def save(self, *args, **kwargs):
        super().save()
