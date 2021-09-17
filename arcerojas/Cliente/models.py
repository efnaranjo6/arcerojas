from django.db import models
from TipoCliente.models import TipoCliente
from TipoIdentificacion.models import TipoIdentificacion
# Create your models here.
class Cliente(models.Model):
    TipoIdentificacion = models.ForeignKey(TipoIdentificacion, on_delete=models.CASCADE)
    TipoCliente = models.ForeignKey(TipoCliente, on_delete=models.CASCADE)
    NombreCliente = models.CharField(max_length=200)
    numeroIdentificacion = models.CharField(max_length=200) 
    def __str__(self):
        return '{}'.format(self.NombreCliente)
class Meta:
    verbose_name_plural='Clientes'    

