import pandas as pd
from google.cloud import documentai_v1 as documentai

def documentParser(image_content):
    # Configurar los parámetros directamente dentro de la función
    project_id = "389568752756"
    location = "us"
    processor_id = "405125601c154e37"
    mime_type = "image/jpeg"  # Asumiendo que tienes un tipo MIME predeterminado

    """
    Processes a document using the Document AI Online Processing API and returns a dictionary with relevant data.
    """
    opts = {"api_endpoint": f"{location}-documentai.googleapis.com"}
    documentai_client = documentai.DocumentProcessorServiceClient(client_options=opts)
    resource_name = documentai_client.processor_path(project_id, location, processor_id)

    raw_document = documentai.RawDocument(content=image_content, mime_type=mime_type)
    request = documentai.ProcessRequest(name=resource_name, raw_document=raw_document)
    result = documentai_client.process_document(request=request)

    # Inicializar un diccionario para los datos relevantes
    relevant_data = {
        "anio": "",
        "bimestre": "",
        "consumo_resultante": "",
        "cta_2_fecha_corte": "",
        "cta_2_primer_vencimiento": "",
        "cta_2_primer_vencimiento_importe": "",
        "cta_2_segundo_vencimiento": "",
        "cta_2_segundo_vencimiento_importe": "",
        "detalle_facturacion": "",
        "dias_medidos": "",
        "domicilio_suministro": "",
        "fecha_corte": "",
        "fecha_emision": "",
        "fecha_lectura_actual": "",
        "fecha_lectura_anterior": "",
        "id_factura": "",
        "id_suministro": "",
        "lectura_actual": "",
        "lectura_anterior": "",
        "nombre_titular": "",
        "nro_medidor": "",
        "primer_vencimiento": "",
        "primer_vencimiento_importe": "",
        "segundo_vencimiento": "",
        "segundo_vencimiento_importe": "",
        "tarifa": "",
        "tipo_consumo": "",
        "total_factura": ""
    }
    # Imprimir el resultado en la consola
    print(result)
    
    # Extraer datos relevantes del resultado del procesamiento
    for entity in result.document.entities:
        if entity.type_ in relevant_data:
            relevant_data[entity.type_] = entity.mention_text

    return relevant_data

## Pruebo en la consola



