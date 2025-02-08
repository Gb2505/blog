from django.db import models

# Create your models here.
class Blog(models.Model):
    apelido = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    senha = models.CharField(max_length=50, null=False, blank=False)

    def  __str__(self):
        return self.apelido
