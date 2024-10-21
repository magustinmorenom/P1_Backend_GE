from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import FacturaModel
from .documentParserAi import documentParser
from datetime import datetime
import json

def parse_date_to_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return datetime(1900, 9, 9).date()

def parse_decimal(decimal_str):
    try:
        return float(decimal_str.replace('.', '').replace(',', '.'))
    except ValueError:
        return 0.0

@csrf_exempt
def registrarScanView(request):
    if request.method == 'POST':
        if 'image' in request.FILES:
            image = request.FILES['image']
            image_content = image.read()
            relevant_data = documentParser(image_content)
            return JsonResponse(relevant_data)
        else:
            data = json.loads(request.body)
            factura = FacturaModel(
                anio=int(data.get("anio", 0)),
                bimestre=int(data.get("bimestre", 0)),
                consumo_resultante=int(data.get("consumo_resultante", 0)),
                cta_2_fecha_corte=parse_date_to_date(data.get("cta_2_fecha_corte", "")),
                cta_2_primer_vencimiento=parse_date_to_date(data.get("cta_2_primer_vencimiento", "")),
                cta_2_primer_vencimiento_importe=parse_decimal(data.get("cta_2_primer_vencimiento_importe", "0.0")),
                cta_2_segundo_vencimiento=parse_date_to_date(data.get("cta_2_segundo_vencimiento", "")),
                cta_2_segundo_vencimiento_importe=parse_decimal(data.get("cta_2_segundo_vencimiento_importe", "0.0")),
                detalle_facturacion=data.get("detalle_facturacion", ""),
                dias_medidos=int(data.get("dias_medidos", 0)),
                domicilio_suministro=data.get("domicilio_suministro", ""),
                fecha_corte=parse_date_to_date(data.get("fecha_corte", "")),
                fecha_emision=parse_date_to_date(data.get("fecha_emision", "")),
                fecha_lectura_actual=parse_date_to_date(data.get("fecha_lectura_actual", "")),
                fecha_lectura_anterior=parse_date_to_date(data.get("fecha_lectura_anterior", "")),
                id_factura=int(data.get("id_factura", 0)),
                id_suministro=int(data.get("id_suministro", 0)),
                lectura_actual=int(data.get("lectura_actual", 0)),
                lectura_anterior=int(data.get("lectura_anterior", 0)),
                nombre_titular=data.get("nombre_titular", ""),
                nro_medidor=int(data.get("nro_medidor", 0)),
                primer_vencimiento=parse_date_to_date(data.get("primer_vencimiento", "")),
                primer_vencimiento_importe=parse_decimal(data.get("primer_vencimiento_importe", "0.0")),
                segundo_vencimiento=parse_date_to_date(data.get("segundo_vencimiento", "")),
                segundo_vencimiento_importe=parse_decimal(data.get("segundo_vencimiento_importe", "0.0")),
                tarifa=data.get("tarifa", ""),
                tipo_consumo=data.get("tipo_consumo", ""),
                total_factura=parse_decimal(data.get("total_factura", "0.0")),
                file_name=data.get("file_name", "")
            )
            factura.save()
            return JsonResponse(data)
    return JsonResponse({'error': 'Método no permitido'}, status=405)
