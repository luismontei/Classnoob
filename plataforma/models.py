from django.db import models

class Link(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField()
    data_criacao = models.DateField(auto_now_add=True)
    arquivo = models.FileField(upload_to='uploads/', default="",blank=True)

    def __str__(self):
        return str(self.titulo)

class Comentario(models.Model):
    name = models.CharField(max_length=50, default="")
    explicacao = models.TextField()
    arquivo = models.FileField(upload_to='uploads/', default="",blank=True)

    def __str__(self):
        return str(self.name)




