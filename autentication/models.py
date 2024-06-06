from django.db import models


class Cargos(models.Model):
    """
    Params : @nome -> STR | @lotacao -> STR
    """

    nome = models.CharField(
        verbose_name="Nome do cargo",
        null=True,
        blank=True,
        max_length=100,
    )
    lotacao = models.CharField(
        verbose_name="Lotação",
        null=True,
        blank=True,
        max_length=100,
    )

    def __str__(self) -> str:
        return f"{self.nome} - {self.lotacao}"


class Pessoa(models.Model):
    """
    Params : @nome -> STR | @email -> STR | @senha -> STR
    """

    nome = models.CharField(
        verbose_name="Nome",
        null=True,
        blank=True,
        max_length=100,
    )
    email = models.EmailField(
        verbose_name="Email",
        null=True,
        blank=True,
    )
    senha = models.CharField(
        verbose_name="Senha",
        null=True,
        blank=True,
        max_length=100,
    )
    cargo = models.ManyToManyField(
        Cargos,
        verbose_name="Cargos",
        blank=True,
    )

    def __str__(self) -> str:
        return f"{self.nome} - {self.email} - {self.senha}"
