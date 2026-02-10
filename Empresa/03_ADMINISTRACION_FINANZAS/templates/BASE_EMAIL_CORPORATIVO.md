<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        /* Base typography */
        body {
            margin: 0;
            padding: 0;
            background-color: #ffffff;
            -webkit-text-size-adjust: 100%;
            -ms-text-size-adjust: 100%;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            color: #374151; /* Dark gray for premium look */
        }
        
        /* Link styles */
        a {
            color: #1976d2;
            text-decoration: none;
            font-weight: 500;
        }

        /* Bold styles as requested */
        strong, b {
            color: #5b5d61;
            font-weight: 700;
        }

        /* Mobile adjustments */
        @media only screen and (max-width: 600px) {
            .email-container {
                width: 100% !important;
                padding: 20px !important;
            }
            .content-td {
                padding: 0 20px 40px 20px !important;
            }
        }
    </style>
</head>
<body style="margin: 0; padding: 0; background-color: #ffffff;">
    <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #ffffff;">
        <tr>
            <td align="center" style="padding: 20px 0;">
                <table border="0" cellpadding="0" cellspacing="0" width="650" class="email-container" style="background-color: #ffffff; border-collapse: collapse;">
                    <!-- Logo Section -->
                    <tr>
                        <td align="left" style="padding: 20px 50px 40px 50px;">
                            <img src="cid:logo_qai" alt="The QAI Company" style="display: block; height: 60px; width: auto; border: 0;">
                        </td>
                    </tr>
                    
                    <!-- Main Content Section -->
                    <tr>
                        <td align="left" class="content-td" style="padding: 0 50px 20px 50px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 16px; line-height: 1.6; color: #374151;">
                            <div style="margin-bottom: 25px;">
                                {{CUERPO_EMAIL}}
                            </div>

                            <!-- Closing / Signature Section (Matches CIAL Model) -->
                            <div style="margin-top: 35px;">
                                <p style="margin: 0 0 24px 0;">Saludos,</p>
                                <p style="margin: 0 0 24px 0;">Atentamente,</p>
                                
                                <div style="margin-top: 24px; line-height: 1.5;">
                                    <span style="display: block; font-size: 16px; font-weight: 700; color: #5b5d61; margin-bottom: 2px;">{{NOMBRE_AGENTE}}</span>
                                    <span style="display: block; font-size: 15px; color: #4b5563; margin-bottom: 4px;">{{ROL_AGENTE}} @ QAI</span>
                                    <a href="https://qai.cl" style="font-size: 15px;">The QAI Company SpA</a>
                                </div>
                            </div>
                        </td>
                    </tr>

                    <!-- Footer Section -->
                    <tr>
                        <td align="center" style="padding: 60px 50px 40px 50px;">
                            <table border="0" cellpadding="0" cellspacing="0" width="100%">
                                <tr>
                                    <td style="border-top: 1px solid #f3f4f6; padding-top: 30px;" align="center">
                                        <p style="margin: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 12px; color: #9ca3af; line-height: 1.5;">
                                            <strong style="color: #5b5d61;">The QAI Company SpA</strong> | Bucarest 17 Dp 58, Providencia, Santiago, RM.
                                        </p>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
