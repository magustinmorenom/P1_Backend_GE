from FacturasEndpoint.models import PagoFactura
from django.db.models import F


# Vista para actualizar el estado del pago
def actualizar_estado_pago_view(request):
    if request.method == 'POST':
        id_factura = request.POST.get('id_factura')
        id_suministro = request.POST.get('id_suministro')
        nro_cuota = request.POST.get('nro_cuota')
        nuevo_estado = request.POST.get('nuevo_estado')
        
        resultado = PagoFactura.actualizar_estado_pago(id_factura, id_suministro, nro_cuota, nuevo_estado)
        return JsonResponse({'mensaje': resultado})
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)
