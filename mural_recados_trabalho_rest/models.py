from django.db import models


class Recado(models.Model):
    texto = models.TextField(verbose_name="Recado", max_length=5000, blank=False, null=False)
    apelido_usuario = models.CharField(verbose_name="Apelido", max_length=5000, blank=False, null=False,
                                       help_text="Pessoa que mandou a mensagem.")
