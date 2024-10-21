## Compara la variacion del consumo con el bimestre anterior



from django.db.models import Sum
from FacturasEndpoint.models import FacturaModel

def compararBimestres(id_factura):
    # Obtener la factura específica para extraer el año y bimestre
    factura = FacturaModel.objects.get(id_factura=id_factura)
    anio_actual = factura.anio
    bimestre = factura.bimestre
    anio_anterior = anio_actual - 1

    # Obtener el total del bimestre actual
    total_bimestre_actual = FacturaModel.objects.filter(anio=anio_actual, bimestre=bimestre).aggregate(
        total=Sum('total_factura')
    )['total'] or 0

    # Validar si hay datos para el año anterior
    if not FacturaModel.objects.filter(anio=anio_anterior, bimestre=bimestre).exists():
        return {
            'mensaje': 'No hay datos para el bimestre anterior'
        }

    # Obtener el total del bimestre del año anterior
    total_bimestre_anterior = FacturaModel.objects.filter(anio=anio_anterior, bimestre=bimestre).aggregate(
        total=Sum('total_factura')
    )['total'] or 0

    # Calcular la variación porcentual
    if total_bimestre_anterior == 0:
        variacion_porcentual = 0
    else:
        variacion_porcentual = ((total_bimestre_actual - total_bimestre_anterior) / total_bimestre_anterior) * 100

    # Redondear el resultado y convertirlo a entero
    variacion_porcentual_redondeada = round(variacion_porcentual)

    # Crear el objeto de retorno
    resultado = {
        'bimestre': bimestre,
        'anio_actual': anio_actual,
        'anio_anterior': anio_anterior,
        'consumo_anio_actual': total_bimestre_actual,
        'consumo_anio_anterior': total_bimestre_anterior,
        'variacion_consumo': total_bimestre_actual - total_bimestre_anterior,
        'porcentaje_variacion': variacion_porcentual_redondeada
    }

    return resultado

