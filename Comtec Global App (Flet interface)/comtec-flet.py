# Created by: Tomas Contreras, student from BYU Idaho

import flet as ft
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
import threading

def main(page: ft.Page):
    # Establecer el tamaño de la ventana
    page.window_width = 400
    page.window_height = 700 
    #alinear elementos al centro
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    #color del background
    #page.bgcolor = ft.colors.GREY_300
    #o poner tema
    page.theme_mode = ft.ThemeMode.LIGHT

    page.window_max_width = 400
    page.window_max_height = 700
    page.window_min_width = 400
    page.window_min_height = 700

    #agregar imagen encabezado
    img = ft.Container(
            image_src='https://comtecglobal.cl/wp-content/uploads/2021/08/Logotipo-Comtec-Global-Color.png',
            image_fit=ft.ImageFit.COVER,
            expand=False,
            width= 320,
            height=100,
            margin=15
        )
    

    #Agregar label
    title = ft.Text("Changes Form", theme_style=ft.TextThemeStyle.TITLE_LARGE, font_family= "Bold", weight= ft.FontWeight.BOLD, color= "#03045e")


    # Crear un campo de texto
    file_name = ft.TextField(label="File name: ", width=300)
    
    local_name = ft.TextField(label="Local name: ", width=300)
    new_local_name = ft.TextField(label="New local name: ", width=300)
    
    serial_number = ft.TextField(label="Serial number: ", width=300, keyboard_type= ft.KeyboardType.NUMBER,
            input_filter=ft.InputFilter(
            allow=True,
            regex_string=r"[0-9+]",
            replacement_string="",)
    )
    
    new_serial_number = ft.TextField(label="New serial number: ", width=300, keyboard_type= ft.KeyboardType.NUMBER,
            input_filter=ft.InputFilter(
            allow=True,
            regex_string=r"[0-9+]",
            replacement_string="",)
    )

    destinatario = ft.TextField(label="Email: ", width=300)


    # Función para manejar el clic del botón // CREAR ARCHIVO TXT CON INFO OBTENIDA
    def txt_file(e):
        file_path = file_name.value + ".txt"
        with open(file_name.value + ".txt", "w") as file:
            file.write(f"File name: {file_name.value}\n")
            file.write(f"Local name: {local_name.value}\n")
            file.write(f"New local name: {new_local_name.value}\n")
            file.write(f"Serial number: {serial_number.value}\n")
            file.write(f"New serial number: {new_serial_number.value}\n")
        page.bgcolor = ft.colors.BLACK
        page.update()


        # Enviar email en un hilo separado
        threading.Thread(
            target=send_email,
            args=(
                f"{destinatario.value}",
                "Archivo python",
                "Hola, adjunto el archivo generado.",
                file_path,
                "tcontreras@comtecglobal.cl",
                "Tsr.646023",
                "smtp-email.outlook.com",
                587
            )
        ).start()
        
        #cerrar app despues de un leve tiempo
        page.update()  # Puedes ajustar el tiempo de espera
        page.window_close()

    # Crear un botón
    submit_button = ft.ElevatedButton("Submit", on_click=txt_file, color= "#03045e", elevation= 8, width= 250, height= 60, bgcolor= "#5FB8FC")


    # Crear fila para centrar elementos
    row_elements = ft.Column(
        controls = [file_name, 
                    local_name,
                    new_local_name,
                    serial_number,
                    new_serial_number,
                    destinatario],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10
    )

    # Crear una fila para centrar el botón
    button_container = ft.Row(
        controls=[submit_button],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
    )
    

    #agregar objeto a la app
    page.add(img, title, row_elements, button_container)


    def send_email(destinatario, asunto, body, adjunt_file, remitente, password_smtp, server_smtp, port_smtp):
        #create email message
        message = MIMEMultipart()
        message["From"] = remitente
        message["To"] = destinatario
        message["Subject"] = asunto

        remitente = "tcontreras@comtecglobal.cl"
        destinatario = ""
        asunto = "Cambio de equipos // sede"
        body = f"Estimado/a, documento de cambio desde {local_name.value}, favor revisar y actualizar datos."
        password_smtp = "Tsr.646023"
        server_smtp = "smtp.office365.com"
        port_smtp = 587

        #add message body
        message.attach(MIMEText(body, "plain"))

        # Adjuntar archivo
        with open(adjunt_file, "rb") as file:
            adjunto = MIMEBase("application", "octet-stream")
            adjunto.set_payload(file.read())
            encoders.encode_base64(adjunto)
            adjunto.add_header("content-Disposition", f"attachment; filename= {os.path.basename(adjunt_file)}")
            message.attach(adjunto)
            
        #connect to smtp servers
        with smtplib.SMTP(server_smtp, port_smtp) as smtp:
            smtp.starttls()
            smtp.login(remitente, password_smtp)
            smtp.send_message(message)


        # Enviar email al hacer clic en el botón
        submit_button.on_click = lambda e: (txt_file(e), send_email(destinatario, asunto, body, adjunt_file, remitente, password_smtp, server_smtp, port_smtp))



ft.app(target=main)

