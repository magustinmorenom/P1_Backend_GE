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
   
    # Inicializar un diccionario para los datos relevantes
    relevant_data = {
        "anio": "2024",
        "bimestre": "6",
        "consumo_resultante": "156447",
        "cta_2_fecha_corte": "06-06-2024",
        "cta_2_primer_vencimiento": "12-05-2024",
        "cta_2_primer_vencimiento_importe": "15090",
        "cta_2_segundo_vencimiento": "29-05-2024",
        "cta_2_segundo_vencimiento_importe": "15795",
        "detalle_facturacion": "Detalle de facturación Fictisio",
        "dias_medidos": "60",
        "domicilio_suministro": "Calle Fantasía 123",
        "fecha_corte": "08-05-2024",
        "fecha_emision": "28-03-2024",
        "fecha_lectura_actual": "28-03-2024",
        "fecha_lectura_anterior": "25-01-2024",
        "id_factura": "4398467123",
        "id_suministro": "502982101",
        "lectura_actual": "77502",
        "lectura_anterior": "76171",
        "nombre_titular": "AGUSTIN MORENO",
        "nro_medidor": "310342",
        "primer_vencimiento": "12-04-2024",
        "primer_vencimiento_importe": "15090",
        "segundo_vencimiento": "27-04-2024",
        "segundo_vencimiento_importe": "15795",
        "tarifa": "T1",
        "tipo_consumo": "Tipo de consumo Fictisio",
        "total_factura": "30181"
    }
    # Imprimir el resultado en la consola
    print(relevant_data)
    print(raw_document.display_name)
    
    ## En esta parte extreaeríamos perloque hacemos se le damos los datos
    # hardcodeados para probar. 
   

    return relevant_data

## Pruebo en la consola



