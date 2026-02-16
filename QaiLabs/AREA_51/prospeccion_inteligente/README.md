# Email Automation Script for CirclePack Contacts

This script sends personalized HTML emails to active contacts from the `circle_pack_data_v2_1.csv` file, using the content from `Texto_mail.md` and embedding `logo_lite.png`.

## Prerequisites

- Python 3.x
- Install dependencies: `pip install pandas`
- Ensure the following files are in the same directory:
  - `circle_pack_data_v2_1.csv` (contact data)
  - `logo_lite.png` (company logo)
  - `email_sender.py` (this script)

## Configuration

SMTP settings are hardcoded in the script based on `Mail_settings.md`. Update if necessary.

- Server: mail.latinarq.com
- Port: 587 (TLS)
- Sender: iliana.alzurutt@latinarq.com
- Password: [configured]

## Usage

1. **Test Mode**: Run `python email_sender.py` to send a test email to the sender's address. Check the email for formatting.

2. **Full Send**: After validating the test email, uncomment the full send section in `if __name__ == '__main__':` and run again.

## Filtering Criteria

Contacts are filtered where:
- `Activo` == 'Sí'
- `Nombre` is not null/empty
- `Correo` != 'No encontrado'

## Email Template

- Subject: "¿Y si tu stand también fuera circular en Circlepack 2026?"
- HTML body with embedded logo, personalized greeting, and content from `Texto_mail.md`.
- Signature includes sender details.

## Security Notes

- Password is hardcoded; consider using environment variables for production.
- Ensure SMTP credentials are secure.

## Output

Prints success/failure for each email sent.
