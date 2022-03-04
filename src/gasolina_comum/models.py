from django.db import models


class GasolinaComum(models.Model):
    """
    Modelo contendo os campos presentes na raspagem de dados. O campo extra
    indica como esse dado foi gerado, se foi pela raspagem ou manualmente 
    criado pelo usuário.
    """
    tipo = models.CharField(max_length=100)
    valor_unitario = models.DecimalField(max_digits=5, decimal_places=3)
    valor_ultima_venda = models.DecimalField(max_digits=5, decimal_places=3)
    tempo_ultima_venda = models.CharField(max_length=50)
    contribuinte = models.CharField(max_length=200)
    codigo = models.PositiveIntegerField()
    raspagem = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.tipo} - R$ {self.valor_unitario}'

    class Meta:
        verbose_name_plural = 'Gasolina Comum'


class Registro(models.Model):
    """
    Modelo para o resgitro das datas nas quais os dados foram coletados.
    """
    tempo = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tempo
