from django.db import models

# Create your models here.

class Pergunta(models.Model):
    pergunta_texto = models.CharField(max_length=200)
    pub_data = models.DateTimeField('Data da Publicação')

    def __str__(self):
        return self.pergunta_texto

class Resposta(models.Model):
    pergunta = models.ForeignKey(Pergunta)
    resposta_texto = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.resposta_texto