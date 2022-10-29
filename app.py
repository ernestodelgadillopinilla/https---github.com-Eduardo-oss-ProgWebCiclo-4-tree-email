from tkinter import CENTER
from unicodedata import name
from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
load_dotenv()
from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient


app = Flask(__name__)
@app.route("/")
def hello_world():    
    return "<h1>Bienvenidos a nuestra pantilla de envío de correos electrónicos</h1>"
    
@app.route("/envio-correo")
def email():
    destino = request.args.get('correo_destino')
    asunto = request.args.get('asunto')
    mensaje = request.args.get('contenido')
    message = Mail(
        from_email='enestodelgadillo@gmail.com',
        to_emails=destino,
        subject=asunto,
        html_content=mensaje)
    
    try:
        sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        return 'Correo electrónico enviado'
    except Exception as e:
        print(e.message)
        return 'Error enviando el mensaje'
