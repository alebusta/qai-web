# Conector SII - Área 51

> **Estado**: 🟡 En Desarrollo (Fase 1)  
> **Última Actualización**: 11-Ene-2026  
> **Responsable**: Nzero (Agente Arquitecto)

## 📋 Descripción
Este es un experimento para desarrollar un conector con el Servicio de Impuestos Internos (SII) de Chile, enfocado en la automatización de declaraciones de IVA (F29), tanto para casos sin movimiento como con movimientos.

## 🎯 Objetivos
- [ ] Investigar y documentar las opciones de integración con el SII
- [ ] Implementar autenticación segura (ClaveÚnica)
- [x] Desarrollar flujo de declaración F29 sin movimiento (RUT/clave)
- [x] Generar declaración F29 sin movimiento en JSON
- [ ] Crear propuesta de declaración con movimientos
- [ ] Documentar hallazgos y limitaciones

## 🛠️ Tecnologías
- Python 3.9+
- Selenium/Playwright para automatización de navegador (si es necesario)
- Bibliotecas de manejo de PDF y XML
- Entorno virtual (venv)

## 🚀 Instalación
```bash
# Clonar el repositorio
cd QaiLabs/AREA_51/sii_connector

# Crear entorno virtual
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Instalar dependencias
pip install -r requirements.txt
```

## 📂 Estructura del Proyecto
```
sii_connector/
├── README.md          # Este archivo
├── requirements.txt   # Dependencias
├── sii_auth.py        # Módulo de autenticación
├── f29_generator.py   # Generador de F29
└── tests/             # Pruebas unitarias
    └── __init__.py
```

## 🔐 Seguridad
- Las credenciales NO deben guardarse en el código
- Usar variables de entorno para datos sensibles
- No subir archivos de configuración con credenciales

## 📝 Notas de Desarrollo
- Este es un proyecto experimental en el Área 51
- El código puede ser desechable
- Documentar todo aprendizaje en este README

## ✅ Flujo de Autenticación + Declaración sin Movimiento
1. Crear `.env` en esta carpeta:
   ```
   SII_RUT=12345678-9
   SII_PASSWORD=tu_contraseña
   ```
2. Activar el entorno virtual e instalar dependencias (`pip install -r requirements.txt`).
3. Ejecutar en modo visible (recomendado para la primera vez):
   ```bash
   python -c "from flows.f29_no_movement import declare_f29_sin_movimiento; declare_f29_sin_movimiento(periodo='2025-12', headless=False)"
   ```
4. Alternativas útiles:
   - Ejecutar el script directamente (usa período anterior por defecto):
     ```bash
     python flows/f29_no_movement.py
     ```
   - Ejecutar en modo headless:
     ```bash
     python -c "from flows.f29_no_movement import declare_f29_sin_movimiento; declare_f29_sin_movimiento(headless=True)"
     ```
   - Ajustar retención de capturas (por defecto: 30 días):
     ```bash
     python -c "from flows.f29_no_movement import declare_f29_sin_movimiento; declare_f29_sin_movimiento(cleanup_screenshots_days=7)"
     ```
5. Qué hace el flujo:
   - Autentica con RUT/clave en `https://www4.sii.cl/consdcvinternetui/`.
   - Abre `https://www4.sii.cl/propuestaf29ui/index.html#/default`, selecciona período (si se especifica) y elige “Sin movimiento”.
   - Pulsa **Enviar** y espera confirmación.
6. Resultados y mensajes esperados:
   - Si el período ya está declarado, el flujo termina con estado `ya_declarado` y guarda la captura en `output/screenshots/<run_id>/sii_f29_periodo_ya_declarado.png`.
   - Si el envío es exitoso, guarda confirmación y HTML en `output/`.
7. Artefactos generados:
   - Capturas por ejecución: `output/screenshots/<run_id>/sii_initial_page.png`, `sii_before_login.png`, `sii_after_login.png`, `sii_f29_step1.png`, `sii_f29_antes_de_enviar.png`, etc.
   - Confirmación final: `output/f29_sin_mov_YYYY-MM_confirmacion.png`.
   - HTML de respaldo: `output/f29_sin_mov_YYYY-MM_confirmacion.html`.
8. Limpieza automática de capturas:
   - Se eliminan carpetas de `output/screenshots/` con más de 30 días (configurable).
9. Si el portal cierra la sesión o cambia la interfaz, el script puede solicitar completar manualmente y presionar Enter para continuar.
10. El enlace al certificado se imprime en consola (`certificado_href`) si está disponible.

## 📅 Próximos Pasos
1. [ ] Investigar API/RPA del SII
2. [ ] Implementar autenticación básica
3. [ ] Desarrollar generador de F29 sin movimiento
4. [ ] Probar en entorno de pruebas del SII

## 📚 Recursos
- [Documentación oficial SII](https://www.sii.cl/)
- [Portal de Pruebas SII](https://www4.sii.cl/consdcvinternetui/)
- [Ley sobre Impuesto a las Ventas y Servicios](https://www.sii.cl/ayudas/ayudas_por_servicios/1953660-ley-iva.html)
