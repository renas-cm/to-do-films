from django.db import models

class Filme(models.Model):
    Title = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.Title}'

class FilmeAssistido(models.Model):
    Title = models.ForeignKey(Filme, on_delete=models.CASCADE)  # 
    Analise = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.Title}'