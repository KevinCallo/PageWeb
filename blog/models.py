from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    CATEGORY_CHOICES = [
        ('recurrencia', 'Recurrencia y árboles'),
        ('fundamentos', 'Fundamentos de programación'),
        ('arreglos', 'Arreglos'),
        ('poo', 'Programación orientada a objetos'),
        ('micro', 'Microeconomía'),
    ]
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title