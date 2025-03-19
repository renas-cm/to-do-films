from django.db import models

class Filme(models.Model):
    Titulo = models.CharField(max_length=255)
    Review = models.TextField(null=True,blank=True)  
    
    def __str__ (self):
        return f'{self.Titulo}'