import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import imaplib
import base64
import os
import datetime

# SMTP settings from Mail_settings.md - using alternative for TLS
smtp_server = 'mail.latinarq.com'
smtp_port = 587
sender_email = 'iliana.alzurutt@latinarq.com'
sender_password = '14675569Ili.'

# Read and filter data
df = pd.read_excel('expositores_circlepack_V2_FINAL.xlsx')
filtered = df[(df['Activo'] == 'Sí') & (df['Nombre'].notna()) & (df['Nombre'] != '') & (df['Correo'] != 'No encontrado')]
sent_emails = ['ventas@nelmaplast.com', 'fsantana@promperu.gob.pe', 'rodrigosilva@cenem.cl', 'procer@procer.cl', 'm.rojo@protechnik.cl', 'mdesmet@rehrig.com', 'prodriguez@rollosdepapel.pe']
filtered = filtered[~filtered['Correo'].isin(sent_emails)]
filtered['Nombre'] = filtered['Nombre'].str.capitalize()

def create_html_body(name):
    html = f"""
    <html>
    <body style="font-family: Arial, sans-serif; margin: 20px;">
    <img src="cid:logo" alt="LITE Logo" width="200" style="margin-bottom: 20px;">
    <p>Hola {name},</p>
    <p>Ya comenzamos a trabajar con expositores que estarán presentes en Circlepack Chile 2026, acompañándolos en el diseño de stands sustentables, reutilizables y coherentes con el espíritu circular de la feria.</p>
    <p>Desde LITE de LatinARQ desarrollamos arquitectura temporal a partir de materiales reciclados y repulpables, con sistemas modulares que permiten reutilizar el stand en distintas ferias, reducir residuos y optimizar la inversión sin sacrificar diseño ni experiencia de marca.</p>
    <p>Nuestro foco está en crear espacios que comuniquen propósito, faciliten la conversación comercial y hagan tangible el compromiso ambiental frente a clientes y partners.</p>
    <p>Si te hace sentido explorar una propuesta para su participación en Circlepack 2026, encantados de coordinar una reunión breve (15–20 min) para conocer sus objetivos y el espacio asignado.</p>
    <p>Quedo atenta para agendar cuando les acomode.</p>
    <p>Un saludo,</p>
    <p><strong>Iliana Alzurutt</strong><br>
    Encargada de Desarrollo de Negocios<br>
    LITE de LatinARQ<br>
    email: iliana.alzurutt@latinarq.com</p>
    </body>
    </html>
    """
    return html

def send_email(to_email, to_name, subject):
    try:
        msg = MIMEMultipart('related')
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = to_email
        html_body = create_html_body(to_name)
        part = MIMEText(html_body, 'html')
        msg.attach(part)
        with open('logo_lite.png', 'rb') as f:
            img = MIMEImage(f.read())
            img.add_header('Content-ID', '<logo>')
            img.add_header('Content-Disposition', 'inline')
            msg.attach(img)
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, msg.as_string())
        server.quit()
        # Save to Sent folder via IMAP
        try:
            imap_server = imaplib.IMAP4_SSL('mail.latinarq.com', 993)
            imap_server.login(sender_email, sender_password)
            imap_server.append('Sent', None, None, msg.as_string())
            imap_server.logout()
        except Exception as e:
            print(f"Failed to save to Sent folder: {str(e)}")
        print(f"Email sent successfully to {to_name} <{to_email}>")
    except Exception as e:
        print(f"Failed to send email to {to_name} <{to_email}>: {str(e)}")

if __name__ == '__main__':
    # Test emails
    test_emails = [
        {'name': 'Iliana', 'email': 'iliana.alzurutt@latinarq.com'},
        {'name': 'Test Outlook', 'email': 'albus@hotmail.com'},
        {'name': 'Test Gmail', 'email': 'afbs77@gmail.com'},
    ]

    print("Starting test phase...")
    for contact in test_emails:
        send_email(contact['email'], contact['name'], '¿Y si tu stand también fuera circular en Circlepack 2026?')

    print("Test phase complete. Review emails and uncomment full send below if ready.")

    # Full send - uncomment after testing
    print("Starting full send...")
    for _, row in filtered.iterrows():
        send_email(row['Correo'], row['Nombre'], '¿Y si tu stand también fuera circular en Circlepack 2026?')
    print("Full send complete.")

    # Update Excel with send date
    today = datetime.date.today()
    df.loc[df['Correo'].isin(filtered['Correo']), 'Fecha_envio'] = today
    df.to_excel('expositores_circlepack_V2_FINAL.xlsx', index=False)
