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

            # Obtener la fecha actual
            fecha_actual = datetime.datetime.now().date()

            # Convertir las fechas de vencimiento a objetos datetime.date
            primer_vencimiento = datetime.datetime.strptime(factura.primer_vencimiento, '%Y-%m-%d').date()
            segundo_vencimiento = datetime.datetime.strptime(factura.segundo_vencimiento, '%Y-%m-%d').date()

            # Crear los registros de PagoFactura correspondientes
            estado_pago_primera = 'Vencido' if primer_vencimiento < fecha_actual else 'Pendiente'
            estado_pago_segunda = 'Vencido' if segundo_vencimiento < fecha_actual else 'Pendiente'

            PagoFactura.objects.create(
                factura=factura,
                suministro=suministro,
                cuota='Primera',
                importe_pago=factura.primer_vencimiento_importe,
                fecha_vencimiento_1=factura.primer_vencimiento,
                fecha_vencimiento_2=factura.segundo_vencimiento,
                fecha_corte=factura.cta_2_fecha_corte,
                estado_pago=estado_pago_primera
            )

            PagoFactura.objects.create(
                factura=factura,
                suministro=suministro,
                cuota='Segunda',
                importe_pago=factura.primer_vencimiento_importe,  # Inicia con el importe del primer vencimiento
                fecha_vencimiento_1=factura.primer_vencimiento,
                fecha_vencimiento_2=factura.segundo_vencimiento,
                fecha_corte=factura.cta_2_fecha_corte,
                estado_pago=estado_pago_segunda
            )

            return JsonResponse({"message": "Factura y pagos creados con éxito"}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)

@csrf_exempt
def actualizarPago(request):
    # Debug en consola para verificar los datos recibidos
    print("Datos recibidos en la vista:", request.body)

    if request.method == 'POST':
        try:
            # Decodifica el cuerpo de la solicitud JSON
            data = json.loads(request.body.decode('utf-8'))
            
            # Extrae los valores del JSON recibido
            id_factura = data.get('id_factura')
            id_suministro = data.get('id_suministro')
            nro_cuota = data.get('nro_cuota')
            nuevo_estado = data.get('nuevo_estado')
            fecha_pago_str = data.get('fecha_pago')
            importe_pago = data.get('importe_pago')
            fecha_pago = datetime.datetime.strptime(fecha_pago_str, '%Y-%m-%d').date() if fecha_pago_str else None
            
            # Debug para verificar los valores extraídos
            print("id_factura:", id_factura)
            print("id_suministro:", id_suministro)
            print("nro_cuota:", nro_cuota)
            print("nuevo_estado:", nuevo_estado)
            print("fecha_pago:", fecha_pago)
            print("importe_pago:", importe_pago)

            # Asegúrate de que los valores existan antes de proceder
            if not all([id_factura, id_suministro, nro_cuota, nuevo_estado]):
                return JsonResponse({'mensaje': 'Faltan datos requeridos.'}, status=400)

            # Aquí iría la lógica para actualizar el estado del pago...
            resultado = PagoFactura.actualizar_estado_pago(id_factura, id_suministro, nro_cuota, nuevo_estado,fecha_pago,importe_pago)
            # return JsonResponse({'mensaje': resultado})

            return JsonResponse({'mensaje': 'Datos recibidos correctamente.', 'resultado': resultado})
        
        except json.JSONDecodeError:
            return JsonResponse({'mensaje': 'Formato de JSON inválido.'}, status=400)

    return JsonResponse({'mensaje': 'Método no permitido.'}, status=405)

def listFacturasView(request):
    if request.method == 'GET':
        try:
            facturas = FacturaModel.objects.all().values()
            return JsonResponse(list(facturas), safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)
    
@csrf_exempt
def getFacturaView(request, id_factura):
    if request.method == 'GET':
        try:
            factura = FacturaModel.objects.filter(id_factura=id_factura).values()
            if factura.exists():
                return JsonResponse(list(factura), safe=False)
            else:
                return JsonResponse({"error": "Factura no encontrada"}, status=404)
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