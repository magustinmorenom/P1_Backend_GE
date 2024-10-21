from django.db.models import Sum
from FacturasEndpoint.models import FacturaModel
from datetime import datetime

def historialConsumoSuministro(id_suministro):
    # Obtener la fecha actual
    fecha_actual = datetime.now()
    anio_actual = fecha_actual.year
    mes_actual = fecha_actual.month

    # Calcular el bimestre actual
    bimestre_actual = (mes_actual + 1) // 2

    # Crear una lista para almacenar el historial de consumo
    historial_consumo = []

    # Variables para seguir el bimestre y año
    bimestre = bimestre_actual
    anio = anio_actual

    # Iterar sobre los últimos 12 bimestres
    for i in range(12):
        # Obtener el total del bimestre actual
        total_bimestre = FacturaModel.objects.filter(anio=anio, bimestre=bimestre, id_suministro=id_suministro).aggregate(
            total=Sum('total_factura')
        )['total'] or 0

        # Agregar los datos al historial de consumo
        historial_consumo.append({
            'anio': anio,
            'bimestre': bimestre,
            'consumo_resultante': total_bimestre
        })

        # Retroceder un bimestre
        bimestre -= 1
        if bimestre < 1:  # Si bimestre es menor a 1, retroceder al bimestre 6 del año anterior
            bimestre = 6
            anio -= 1

    return historial_consumo
