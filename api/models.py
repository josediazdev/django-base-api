from django.db import models
from django.utils import timezone

# Create your models here.
class Employees(models.Model):
    id_card = models.IntegerField()
    name = models.CharField(max_length=50)
    entry_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Identificador: {self.id_card}, Nombre: {self.name}'
