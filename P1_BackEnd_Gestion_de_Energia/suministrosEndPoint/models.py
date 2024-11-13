from django.db import models

# Tabla de suministros
class SuministroModel(models.Model):
    id_suministro = models.CharField(max_length=255, primary_key=True)  # Definir como clave primaria
    nombre_suministro = models.CharField(max_length=255)
    geolocalizacion = models.CharField(max_length=255, null=True, blank=True)
    domicilio = models.CharField(max_length=255, null=True, blank=True)
    nro_medidor = models.CharField(max_length=255, null=True, blank=True)
    TARIFA_CHOICES = [
        ('T1', 'T1'),
        ('T2', 'T2'),
        ('T3', 'T3'),
        ('A', 'A'),
    ]
    tarifa = models.CharField(max_length=255, choices=TARIFA_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.nombre_suministro

# Tabla de etiquetas
class EtiquetasSuministroModel(models.Model):
    nombre_etiqueta = models.CharField(max_length=255)
    color_etiqueta = models.CharField(max_length=255, null=True, blank=True)
    id_etiqueta = models.AutoField(primary_key=True)

    def __str__(self):
        return self.nombre_etiqueta

# Tabla de asociación entre suministros y etiquetas
class SuministroEtiqueta(models.Model):
    suministro = models.ForeignKey(SuministroModel, on_delete=models.CASCADE, to_field='id_suministro')
    etiqueta = models.ForeignKey(EtiquetasSuministroModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.suministro} - {self.etiqueta}'
