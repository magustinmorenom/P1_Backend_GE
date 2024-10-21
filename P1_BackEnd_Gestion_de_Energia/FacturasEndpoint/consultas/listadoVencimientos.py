from FacturasEndpoint.models import PagoFactura
from collections import defaultdict

def listarVencimientos(id_factura):
    # Crear un diccionario que almacenará los datos de la factura específica
    factura_dict = defaultdict(list)

    # Consulta para obtener los datos necesarios solo para el id_factura proporcionado
    resultados = PagoFactura.objects.filter(factura__id_factura=id_factura).values(
        'factura__id_factura',
        'cuota',
        'fecha_vencimiento_1',
        'fecha_vencimiento_2',
        'fecha_corte',
        'fecha_pago',
        'estado_pago',
        'metodo_pago'
    ).order_by('cuota')

    # Agrupar los resultados por id_factura (aunque en este caso solo hay uno)
    for resultado in resultados:
        factura_dict[resultado['factura__id_factura']].append({
            'cuota': resultado['cuota'],
            'fecha_vencimiento_1': resultado['fecha_vencimiento_1'],
            'fecha_vencimiento_2': resultado['fecha_vencimiento_2'],
            'fecha_pago': resultado['fecha_pago'],
            'estado_pago': resultado['estado_pago'],
            'metodo_pago': resultado['metodo_pago'],
            'fecha_corte': resultado['fecha_corte'],
        })

    # Devolver los datos de la factura específica
    return factura_dict[id_factura] if id_factura in factura_dict else None

