from django.db import models

# Create your models here.
class Autor(models.Model):
    nome = models.CharField('Nome', max_length=100)
    data_nascimento = models.DateField('Data de Nascimento')
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.nome

class Artigo(models.Model):
    titulo = models.CharField('Titulo', max_length=100)
    resumo = models.TextField('Resumo')
    autores = models.ManyToManyField(Autor)
    criado = models.DateTimeField('Criado em', auto_now_add=True)

    def __str__(self):
        return self.titulo

