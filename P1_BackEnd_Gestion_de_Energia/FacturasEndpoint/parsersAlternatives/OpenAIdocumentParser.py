from openai import OpenAI

client = OpenAI(api_key='sk-None-xeSwX1mKG2vmzyJ28J2jT3BlbkFJxVRaedxAAEkBFjGdWEVL')
import pytesseract
from PIL import Image
import json
import os

# Configura tu clave de API de OpenAI directamente

# Configura la ruta de Tesseract en tu sistema
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

def convertir_imagen_a_texto(ruta_imagen):
    # Verifica si el archivo existe
    if not os.path.exists(ruta_imagen):
        raise FileNotFoundError(f"El archivo no se encuentra en la ruta especificada: {ruta_imagen}")

    # Abre la imagen y usa Tesseract para convertirla a texto
    img = Image.open(ruta_imagen)
    texto = pytesseract.image_to_string(img)
    return texto

def documentParser(factura_texto):
    prompt = f"""
    Extrae la siguiente información de la factura:
    Nombre titular
    Domicilio suministro
    Número de medidor
    ID suministro
    ID factura
    Tarifa
    Tipo de consumo
    Año
    Bimestre
    Días medidos
    Fecha de lectura anterior
    Fecha de lectura actual
    Lectura anterior
    Lectura actual
    Consumo resultante
    Fecha de corte
    Fecha de emisión
    Fecha de corte (Cuenta 2)
    Primer vencimiento (Cuenta 2)
    Importe primer vencimiento (Cuenta 2)
    Segundo vencimiento (Cuenta 2)
    Importe segundo vencimiento (Cuenta 2)
    Primer vencimiento
    Importe primer vencimiento
    Segundo vencimiento
    Importe segundo vencimiento
    Total factura
    Detalle facturación
    
    Factura:
    {factura_texto}

    Responde en formato JSON.
    """

    # Realiza la solicitud a la API de OpenAI utilizando el nuevo método y modelo
    response = client.chat.completions.create(model="gpt-3.5-turbo",  # Puedes cambiar a "gpt-4" si tienes acceso
    messages=[
        {"role": "system", "content": "Eres un asistente útil."},
        {"role": "user", "content": prompt}
    ],
    max_tokens=1500,
    n=1,
    stop=None,
    temperature=0.5)

    # Procesa la respuesta
    respuesta_texto = response.choices[0].message.content.strip()
    try:
        datos_parseados = json.loads(respuesta_texto)
    except json.JSONDecodeError as e:
        print(f"Error al decodificar el JSON: {e}")
        print(f"Respuesta del modelo: {respuesta_texto}")
        return None
    return datos_parseados

# Ejemplo de uso
ruta_imagen = '/Users/agustin/Downloads/Facturas  Enersa/fa_240510115995_20240717131533.jpg'

try:
    factura_texto = convertir_imagen_a_texto(ruta_imagen)
    datos_parseados = documentParser(factura_texto)
    if datos_parseados:
        print(json.dumps(datos_parseados, indent=4))
except FileNotFoundError as e:
    print(e)
