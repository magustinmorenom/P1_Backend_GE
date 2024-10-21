from suministrosEndPoint.models import SuministroModel  # Importa SuministroModel desde su módulo
from FacturasEndpoint.models import FacturaModel, PagoFactura

def generar_pagos_facturas():
    facturas = FacturaModel.objects.all()
    for factura in facturas:
        print(f"Procesando Factura ID: {factura.id_factura} con Suministro ID: {factura.id_suministro_id}")
        suministros = SuministroModel.objects.filter(id_suministro=factura.id_suministro_id)
        if not suministros.exists():
            print(f"No se encontraron suministros para la Factura ID: {factura.id_factura}")
        for suministro in suministros:
            print(f" - Suministro ID: {suministro.id_suministro}")
            if not PagoFactura.objects.filter(factura=factura, suministro=suministro).exists():
                print(" -- Creando Pago para la Primera Cuota")
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
                print(" -- Creando Pago para la Segunda Cuota")
                PagoFactura.objects.create(
                    factura=factura,
                    suministro=suministro,
                    cuota='Segunda',
                    importe_pago=factura.primer_vencimiento_importe,
                    fecha_vencimiento_1=factura.primer_vencimiento,
                    fecha_vencimiento_2=factura.segundo_vencimiento,
                    fecha_corte=factura.cta_2_fecha_corte,
                    estado_pago='Pendiente'
                )

    print("Proceso completado.")
