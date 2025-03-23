from django.db import models

class Filme(models.Model):
    Title = models.CharField(max_length=255) 
    Watched = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.Title}'
