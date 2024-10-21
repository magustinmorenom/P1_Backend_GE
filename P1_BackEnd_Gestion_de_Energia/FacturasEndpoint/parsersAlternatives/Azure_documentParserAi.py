from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient

# Configuración del endpoint y clave del API
endpoint = "https://moreno2024energia.cognitiveservices.azure.com/"
key = "ef0bff4bd2b44f819c06f3913f92f432"

model_id = "factura-t1"
file_path = "/Users/agustin/Documents/22 Dango/03_Back_End_Energíia/back_end_energia/uploads/scans/Factura06.jpg"

# Crear cliente de análisis de documentos
document_analysis_client = DocumentAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))

# Leer el archivo local en binario
with open(file_path, "rb") as f:
    file_data = f.read()

# Enviar el archivo local para su análisis
poller = document_analysis_client.begin_analyze_document(model_id=model_id, document=file_data)
result = poller.result()

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

# Función para extraer datos relevantes del resultado del procesamiento
def extract_relevant_data(document, relevant_data):
    for name, field in document.fields.items():
        if name in relevant_data:
            relevant_data[name] = field.value if field.value else field.content
    return relevant_data

# Extraer datos relevantes de cada documento analizado
for idx, document in enumerate(result.documents):
    relevant_data = extract_relevant_data(document, relevant_data)

# Imprimir los datos relevantes
for key, value in relevant_data.items():
    print(f"{key}: {value}")

# Función para formatear e imprimir tablas
def print_table(table):
    headers = [cell.content for cell in table.cells if cell.row_index == 0]
    max_row_index = max(cell.row_index for cell in table.cells)
    rows = [
        [cell.content for cell in table.cells if cell.row_index == row_idx]
        for row_idx in range(1, max_row_index + 1)
    ]
    
    print("Tabla:")
    # Imprimir encabezados
    print("\t".join(headers))
    # Imprimir filas
    for row in rows:
        print("\t".join(row))
    print("\n")

# Imprimir tablas encontradas
for table in result.tables:
    print_table(table)

print("-----------------------------------")
