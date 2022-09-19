from django.db import models


# para hacer la migracion mira los comandos aqui:
# https://www.youtube.com/watch?v=ZsJRXS_vrw0

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date publicado')
