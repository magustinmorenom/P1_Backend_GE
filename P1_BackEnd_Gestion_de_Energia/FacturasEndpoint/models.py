from django.db import models
from django.utils import timezone
from suministrosEndPoint.models import SuministroModel

class FacturaModel(models.Model):
    anio = models.IntegerField(null=True)
    bimestre = models.IntegerField(null=True)
    consumo_resultante = models.IntegerField()  # No puede ser null
    cta_2_fecha_corte = models.DateField(null=True)
    cta_2_primer_vencimiento = models.DateField()  # No puede ser null
    cta_2_primer_vencimiento_importe = models.DecimalField(max_digits=10, decimal_places=2)  # No puede ser null
    cta_2_segundo_vencimiento = models.DateField()  # No puede ser null
    cta_2_segundo_vencimiento_importe = models.DecimalField(max_digits=10, decimal_places=2)  # No puede ser null
    detalle_facturacion = models.TextField(null=True)
    dias_medidos = models.IntegerField(null=True)
    domicilio_suministro = models.TextField()  # No puede ser null
    fecha_corte = models.DateField(null=True)
    fecha_emision = models.DateField()  # No puede ser null
    fecha_lectura_actual = models.DateField()  # No puede ser null
    fecha_lectura_anterior = models.DateField()  # No puede ser null
    id_factura = models.CharField(max_length=20, unique=True)  # Cambiado a CharField No puede ser null
    id_suministro = models.ForeignKey(SuministroModel, on_delete=models.CASCADE, to_field='id_suministro')  # Solo puede ser un suministro de la lista de suministros existentes
    lectura_actual = models.IntegerField(null=True)
    lectura_anterior = models.IntegerField(null=True)
    nombre_titular = models.CharField(max_length=255)  # No puede ser null
    nro_medidor = models.IntegerField(null=True)
    primer_vencimiento = models.DateField()  # No puede ser null
    primer_vencimiento_importe = models.DecimalField(max_digits=10, decimal_places=2)  # No puede ser null
    segundo_vencimiento = models.DateField()  # No puede ser null
    segundo_vencimiento_importe = models.DecimalField(max_digits=10, decimal_places=2)  # No puede ser null
    tarifa = models.TextField(null=True)
    tipo_consumo = models.TextField(null=True)
    total_factura = models.DecimalField(max_digits=10, decimal_places=2)  # No puede ser null
    file_name = models.CharField(max_length=255, null=True)
    etiqueta = models.CharField(max_length=255, null=True)  # Asumiendo que 'etiqueta' es un campo de texto
    is_active = models.BooleanField(default=True)  # Campo booleano para marcar si la factura está activa o no
    created_at = models.DateTimeField(auto_now_add=True)  # Campo que guarda la fecha de creación de la factura
    updated_at = models.DateTimeField(auto_now=True)  # Campo que guarda la fecha de la última actualización de la factura
    deleted_at = models.DateTimeField(null=True, blank=True)  # Campo que guarda la fecha de eliminación de la factura

    def __str__(self):
        return self.nombre_titular



class PagoFactura(models.Model):
    
    # Relación con FacturaModel usando id_factura
    factura = models.ForeignKey('FacturaModel', to_field='id_factura', on_delete=models.CASCADE, related_name='pagos')

    # Relación con SuministroModel
    suministro = models.ForeignKey(SuministroModel, on_delete=models.CASCADE, related_name='pagos')
    
    cuota = models.CharField(max_length=7, choices=[('Primera', 'Primera Cuota'), ('Segunda', 'Segunda Cuota')])
    importe_pago = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField(null=True, blank=True)
    estado_pago = models.CharField(max_length=10, choices=[('Pendiente', 'Pendiente'), ('Pagado', 'Pagado'), ('Vencido', 'Vencido')], default='Pendiente')
    fecha_vencimiento_1 = models.DateField()
    fecha_vencimiento_2 = models.DateField()
    fecha_corte = models.DateField()
    metodo_pago = models.CharField(max_length=50, null=True, blank=True)
    comentarios = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = ('factura', 'suministro', 'cuota')

      # Nueva función para actualizar el estado del pago
    @staticmethod
    def actualizar_estado_pago(id_factura, id_suministro, nro_cuota, nuevo_estado, f_pago):
        try:
        # Imprimir en consola los parámetros con los que se va a buscar
            print(f"Buscando en el modelo pago con id_factura: {id_factura}, id_suministro: {id_suministro}, cuota: {nro_cuota}")
            # Obtener el pago específico que coincide con los parámetros
            pago = PagoFactura.objects.get(
                factura__id_factura=id_factura,
                suministro=id_suministro,
                cuota=nro_cuota,
               
            )
            # Actualizar el estado del pago
            pago.estado_pago = nuevo_estado
            pago.fecha_pago = f_pago
            pago.save()
            return f"Estado del pago actualizado a {nuevo_estado} con éxito."
        except PagoFactura.DoesNotExist:
            return "No se encontró un pago con los detalles proporcionados."
        except Exception as e:
            return f"Ocurrió un error al actualizar el estado: {str(e)}"
        
    
    def save(self, *args, **kwargs):
        if self.fecha_pago:
            if self.fecha_pago <= self.fecha_vencimiento_1:
                self.monto_pago = self.factura.primer_vencimiento_importe
            else:
                self.monto_pago = self.factura.segundo_vencimiento_importe
        super(PagoFactura, self).save(*args, **kwargs)

    def __str__(self):
        return f'Pago {self.cuota} - Factura {self.factura.id} - Suministro {self.suministro.id}'

