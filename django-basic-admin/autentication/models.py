from django.db import models
from django.utils.safestring import mark_safe


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
    Params : @nome -> STR | @email -> STR | @senha -> STR | @cargo -> ForeingKey(Cargos)

    """

    foto = models.ImageField(upload_to="fotos")
    nome = models.CharField(
        verbose_name="Nome",
        null=True,
        blank=True,
        max_length=100,
    )
    sobrenome = models.CharField(
        verbose_name="Sobrenome",
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

    def complete_name(self):
        return f"{self.nome} {self.sobrenome}"

    @mark_safe
    def get_image(self):
        return f"<img width='30px' src ='/media/{self.foto}'>"

    class Meta:
        ordering = ["nome"]


class Pedido(models.Model):
    """
    Params : @nome -> STR | @quantidade -> STR | @descrição -> STR | @pessoa -> ForeingKey(Pessoa)
    """

    nome = models.CharField(
        verbose_name="Nome do Pedido",
        max_length=250,
        null=True,
        blank=True,
    )
    quantidade = models.PositiveIntegerField(
        verbose_name="Quantidade de pedidos",
    )
    descricao = models.CharField(
        verbose_name="Descrição do Pedido",
        max_length=250,
        null=True,
        blank=True,
    )
    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return f"{self.nome} - {self.descricao} - {self.quantidade}"
