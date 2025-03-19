from django.db import models

class Filme(models.Model):
    Titulo = models.CharField(max_length=255)
    
    def __str__ (self):
        return f'{self.Titulo}'

class FilmeAssistido(models.Model):
    Titulo = models.ForeignKey(Filme, on_delete=models.CASCADE)
    Analise = models.TextField(null=True,blank=True)
    
    def __str__ (self):
        return f'{self.Titulo}'