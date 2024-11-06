## La consulta toma el consumo de todos lo ssuministros asociados en el mismo bimestre
## realiza un comparativa de los consumos y los ordena de mayor a menor un ranking

from django.db.models import Sum, F, FloatField, ExpressionWrapper
from FacturasEndpoint.models import FacturaModel

def listarPorcentajeBimestre(id_factura):
    # Obtener la factura específica para extraer el año y bimestre
    factura = FacturaModel.objects.get(id_factura=id_factura)
    anio = factura.anio
    bimestre = factura.bimestre

    # Obtener el total de todas las facturas para ese año y bimestre
    total_bimestre = FacturaModel.objects.filter(anio=anio, bimestre=bimestre).aggregate(total=Sum('total_factura'))['total']

    # Consulta para obtener los datos y calcular el porcentaje
    resultados = FacturaModel.objects.filter(anio=anio, bimestre=bimestre).annotate(
        porcentaje_total=ExpressionWrapper(
            F('total_factura') / total_bimestre * 100,
            output_field=FloatField()
        )
    ).values(
        'id_suministro',
        'id_suministro__nombre_suministro',
        'anio',
        'bimestre',
        'total_factura',
        'consumo_resultante',
        'porcentaje_total',
        'id_factura',
    ).order_by('-porcentaje_total')  # Ordenar de mayor a menor por porcentaje_total

    # Añadir el ranking basado en el orden
    resultados_con_ranking = []
    for index, resultado in enumerate(resultados, start=1):
        resultado['ranking'] = index
        resultados_con_ranking.append(resultado)

    return resultados_con_ranking

# Ejemplo de uso:
id_factura = '2403235319'  # Reemplaza esto con el ID de la factura que quieres consultar
datos = listarPorcentajeBimestre(id_factura)


