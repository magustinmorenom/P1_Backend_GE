from flask import Flask, request, jsonify
from flask_wtf.csrf import CSRFProtect, generate_csrf
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json  # Importar json
from django.http import JsonResponse  # Importar JsonResponse para respuestas JSON

app = Flask(__name__)
csrf = CSRFProtect(app)

# ...código existente...

def send_email(email, user, password):
    msg = MIMEMultipart()
    msg['From'] = 'gestiondeenergia@odin.ar'  # Tu correo emisor con nombre
    msg['To'] = email  # Correo del destinatario
    msg['Subject'] = 'Actualización de Usuario Gestion de Energia'

    # Contenido del correo en formato HTML
    html = f"""
    <html>
    <body>
        <h1>Actualizacion de tus Datos en Gestion de Energia</h1>
        <p>Hola,</p>
        <p>Tu cuenta ha sido actualizada exitosamente. Aquí están tus credenciales:</p>
        <p><b>Usuario:</b> {user}</p>
        <p><b>Contraseña:</b> {password}</p>
        <p>Gracias por unirte a nosotros.</p>
    </body>
    </html>
    """
    msg.attach(MIMEText(html, 'html'))

    try:
        # Configuración del servidor SMTP
        server = smtplib.SMTP_SSL('smtp.hostinger.com', 465)  # Usar SMTP_SSL para conexión segura en puerto 465
        server.login('gestiondeenergia@odin.ar', 'Nogoya2025@energia')  # Credenciales de tu correo
        server.sendmail('gestiondeenergia@odin.ar', email, msg.as_string())  # Enviar correo
        server.quit()  # Cerrar conexión
        print("Se actualizaron los datos del usuario y se envío por email")  # Loguear en consola
        return True
    except Exception as e:
        print(f"Error: {e}")  # Loguear errores en consola
        return False

@app.after_request
def set_csrf_cookie(response):
    response.set_cookie('csrf_token', generate_csrf())
    return response

@csrf.exempt
@app.route('/send_credentials', methods=['POST'])
def send_credentials(request):
    if request.method == 'POST':
        try:
            # Parsear los datos JSON de la solicitud
            data = json.loads(request.body)
            email = data.get('email')
            user = data.get('user')
            password = data.get('password')

            # Aquí llamas a tu lógica de envío de correos
            if send_email(email, user, password):  # Reemplaza por tu lógica para enviar correos
                return JsonResponse({"message": "Email sent successfully"}, status=200)
            else:
                return JsonResponse({"message": "Failed to send email"}, status=500)
        except Exception as e:
            return JsonResponse({"error": f"An error occurred: {str(e)}"}, status=500)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)

if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'your_secret_key'
    csrf.init_app(app)
    app.run(debug=True)