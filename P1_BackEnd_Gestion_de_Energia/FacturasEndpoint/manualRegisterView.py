from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import FacturaModel, PagoFactura  # Asegúrate de que el modelo PagoFactura esté importado
from suministrosEndPoint.models import SuministroModel
from django.core.serializers import serialize
import json
from .consultas.listadoPagos import listarPagos
from .consultas.listadoVencimientos import listarVencimientos
from .consultas.porcentajeMismoBimestre import listarPorcentajeBimestre
from .consultas.comparativaBimestreAnterior import compararBimestres
from .consultas.historialDeConumoSuministro import historialConsumoSuministro

import datetime


@csrf_exempt
def manualRegisterView(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Recupera la instancia de SuministroModel utilizando el id_suministro del JSON
            suministro = SuministroModel.objects.get(id_suministro=data.get('id_suministro'))
            
            factura = FacturaModel(
                consumo_resultante=data.get('consumo_resultante'),
                cta_2_primer_vencimiento=data.get('cta_2_primer_vencimiento'),
                cta_2_primer_vencimiento_importe=data.get('cta_2_primer_vencimiento_importe'),
                cta_2_segundo_vencimiento=data.get('cta_2_segundo_vencimiento'),
                cta_2_segundo_vencimiento_importe=data.get('cta_2_segundo_vencimiento_importe'),
                domicilio_suministro=data.get('domicilio_suministro'),
                fecha_emision=data.get('fecha_emision'),
                fecha_lectura_actual=data.get('fecha_lectura_actual'),
                fecha_lectura_anterior=data.get('fecha_lectura_anterior'),
                id_factura=data.get('id_factura'),
                id_suministro=suministro,
                nombre_titular=data.get('nombre_titular'),
                primer_vencimiento=data.get('primer_vencimiento'),
                primer_vencimiento_importe=data.get('primer_vencimiento_importe'),
                segundo_vencimiento=data.get('segundo_vencimiento'),
                segundo_vencimiento_importe=data.get('segundo_vencimiento_importe'),
                total_factura=data.get('total_factura'),
                etiqueta=data.get('etiqueta'),
                anio=data.get('anio'),
                bimestre=data.get('bimestre'),  
                cta_2_fecha_corte=data.get('cta_2_fecha_corte'),
                fecha_corte=data.get('fecha_corte'),
                detalle_facturacion=data.get('detalle_facturacion'),
                dias_medidos=data.get('dias'),
                lectura_anterior=data.get('lectura_anterior'),
                lectura_actual=data.get('lectura_actual'),
                nro_medidor=data.get('nro_medidor'),
                tarifa=data.get('tarifa'),
                tipo_consumo=data.get('tipo_consumo'),
                
                is_active=True
            )
            factura.save()


 # Crear los registros de PagoFactura correspondientes
            PagoFactura.objects.create(
                factura=factura,
                suministro=suministro,
                cuota='Primera',
                importe_pago=factura.primer_vencimiento_importe,
                fecha_vencimiento_1=factura.primer_vencimiento,
                fecha_vencimiento_2=factura.segundo_vencimiento,
                fecha_corte=factura.cta_2_fecha_corte,
                estado_pago='Pendiente'
            )

            PagoFactura.objects.create(
                factura=factura,
                suministro=suministro,
                cuota='Segunda',
                importe_pago=factura.primer_vencimiento_importe,  # Inicia con el importe del primer vencimiento
                fecha_vencimiento_1=factura.primer_vencimiento,
                fecha_vencimiento_2=factura.segundo_vencimiento,
                fecha_corte=factura.cta_2_fecha_corte,
                estado_pago='Pendiente'
            )

            return JsonResponse({"message": "Factura y pagos creados con éxito"}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)

def listFacturasView(request):
    if request.method == 'GET':
        try:
            facturas = FacturaModel.objects.all().values()
            return JsonResponse(list(facturas), safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)

def listPagosView(request):
    if request.method == 'GET':
        try:
            print(f'Ejecutando el llamado a la API listPagosView: {datetime.datetime.now()}')       
            pagos = listarPagos()
            return JsonResponse(pagos, safe=False)
        except Exception as e:
            print(f'Error en la API: {e}')
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)
    
def listVencimientosView (request,id_factura):
    if request.method == 'GET':
        try:
            print(f'Ejecutando el llamado a la API listVencimientosView: {datetime.datetime.now()}')       
            vencimientos = listarVencimientos(id_factura)
            return JsonResponse(vencimientos, safe=False)
        except Exception as e:
            print(f'Error en la API: {e}')
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)
    
def porcentajeBimestreView (request,id_factura):
    if request.method == 'GET':
        try:
            print(f'Ejecutando el llamado a la API porcentajeBimestreView: {datetime.datetime.now()}')       
            porcentajes = listarPorcentajeBimestre(id_factura)
            return JsonResponse(porcentajes, safe=False)
        except Exception as e:
            print(f'Error en la API: {e}')
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)
    
def compararBimestreAnteriorView(request, id_factura):
    if request.method == 'GET':
        try:
            print(f'Ejecutando el llamado a la API compararBimestreAnteriorView: {datetime.datetime.now()}')       
            comparativa = compararBimestres(id_factura)
            return JsonResponse(comparativa)
        except Exception as e:
            print(f'Error en la API: {e}')
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)

def historialConsumoView(request, id_suministro):
    if request.method == 'GET':
        try:
            print(f'Ejecutando el llamado a la API historialConsumoView: {datetime.datetime.now()}')       
            historialConsumos = historialConsumoSuministro(id_suministro)
            return JsonResponse(list(historialConsumos), safe=False)
        except Exception as e:
            print(f'Error en la API: {e}')
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)