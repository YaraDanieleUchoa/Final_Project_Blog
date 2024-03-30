from django.db import models
from categorias.models import Categoria

class Postagem(models.Model):
    titulo = models.CharField(max_length=100, default='')
    mensagem = models.TextField()
    autor = models.CharField(max_length=100, default='')
    imagem = models.ImageField(upload_to='post', null=True, blank=True)
    imagem_url = models.URLField(null=True, blank=True)
    categoria = models.ManyToManyField(Categoria)
    data_postagem = models.DateTimeField(auto_now_add=True)

class Meta:
        verbose_name = 'Postagem'
        verbose_name_plural ='Postagens'