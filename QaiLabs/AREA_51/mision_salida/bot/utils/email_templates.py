"""
QAI HQ Bot — Email Templates
Plantillas HTML para correos corporativos.
"""

def wrap_corporate_template(content_html: str) -> str:
    """
    Envuelve el contenido en la plantilla corporativa de The QAI Company.
    Usa un diseño 'bulletproof' compatible con la mayoría de clientes de correo.
    """
    # Si el contenido ya es HTML completo, no lo envolvemos
    if "<html" in content_html.lower():
        return content_html

    # Convertir saltos de línea a <br> si es texto plano
    if "<br" not in content_html and "<p" not in content_html:
        content_html = content_html.replace("\n", "<br>")

    return f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The QAI Company</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            -webkit-font-smoothing: antialiased;
        }}
        .container {{
            max-width: 600px;
            margin: 0 auto;
            background-color: #ffffff;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        }}
        .header {{
            background-color: #1a1a1a;
            padding: 30px 40px;
            text-align: center;
        }}
        .logo {{
            color: #ffffff;
            font-size: 24px;
            font-weight: 700;
            letter-spacing: 2px;
            text-decoration: none;
            font-family: 'Courier New', Courier, monospace; /* Tech vibe */
        }}
        .content {{
            padding: 40px;
            color: #333333;
            font-size: 16px;
            line-height: 1.6;
        }}
        .footer {{
            background-color: #f8f9fa;
            padding: 20px 40px;
            text-align: center;
            border-top: 1px solid #eeeeee;
        }}
        .footer-text {{
            color: #888888;
            font-size: 12px;
            line-height: 1.4;
            margin: 0;
        }}
        .divider {{
            height: 1px;
            background-color: #e0e0e0;
            margin: 20px 0;
            border: none;
        }}
        a {{
            color: #000000;
            text-decoration: underline;
        }}
    </style>
</head>
<body>
    <div style="padding: 20px;">
        <div class="container">
            <!-- Header -->
            <div class="header">
                <!-- Usamos texto estilizado como logo por ahora -->
                <div class="logo">QAI LABS</div>
            </div>

            <!-- Content -->
            <div class="content">
                {content_html}
            </div>

            <!-- Footer -->
            <div class="footer">
                <p class="footer-text">
                    <strong>The QAI Company SpA</strong><br>
                    Santiago, Chile<br>
                    <a href="https://qai.cl" style="color: #666; text-decoration: none;">www.qai.cl</a>
                </p>
                <div class="divider"></div>
                <p class="footer-text" style="font-size: 10px;">
                    Este mensaje puede contener información confidencial. Si lo has recibido por error, por favor elimínalo.<br>
                    &copy; 2026 The QAI Company. Todos los derechos reservados.
                </p>
            </div>
        </div>
    </div>
</body>
</html>
"""
