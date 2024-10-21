from FacturasEndpoint.models import PagoFactura
from django.db.models import F


def listarPagos():
    # Query to fetch PagoFactura records with related fields
    pago_facturas = PagoFactura.objects.select_related('suministro', 'factura').annotate(
        nombre_suministro=F('suministro__nombre_suministro'),
        id_suministro=F('suministro__id_suministro'),
        anio=F('factura__anio'),
        bimestre=F('factura__bimestre'),
        total_factura=F('factura__total_factura'),
        id_factura=F('factura__id_factura'),
        fecha_lectura_actual=F('factura__fecha_lectura_actual'),
        fecha_lectura_anterior=F('factura__fecha_lectura_anterior'), 
        lectura_actual=F('factura__lectura_actual'),
        lectura_anterior=F('factura__lectura_anterior'),
        dias_medidos=F('factura__dias_medidos'),
        consumo_resultante=F('factura__consumo_resultante')
        
    
    )

    # Print the results
    for pago in pago_facturas:
           data = []
    for pago in pago_facturas:
        data.append({
            'nombre_suministro': pago.nombre_suministro,
            'id_suministro': pago.id_suministro,
            'anio': pago.anio,
            'bimestre': pago.bimestre,
            'cuota':pago.cuota,
            'importe': pago.importe_pago,
            'total_factura': pago.total_factura,
            'id_factura': pago.id_factura,
            'fecha_lectura_actual': pago.fecha_lectura_actual,
            'fecha_lectura_anterior': pago.fecha_lectura_anterior,
            'lectura_actual': pago.lectura_actual,
            'lectura_anterior': pago.lectura_anterior,
            'dias_medidos': pago.dias_medidos,
            'consumo_resultante': pago.consumo_resultante,
            'estado': pago.estado_pago,
            'fecha_pago': pago.fecha_pago,
        })
      
    return data