"""
Módulo de autenticación con el SII (Servicio de Impuestos Internos) de Chile.

Este módulo maneja la autenticación en el portal del SII utilizando diferentes métodos,
como ClaveÚnica o RUT y contraseña.
"""

import os
import time
import unicodedata
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from dotenv import load_dotenv

from f29_generator import F29Generator

# Cargar variables de entorno desde .env
load_dotenv()

class SIIConnectionError(Exception):
    """Excepción personalizada para errores de conexión con el SII."""
    pass

class SIIClient:
    """Cliente para interactuar con el portal del SII."""
    
    # URLs del SII (actualizadas a enero 2026)
    SII_HOME = "https://www4.sii.cl"
    SII_PORTAL = "https://www4.sii.cl/consdcvinternetui/"
    SII_CONSULTA = "https://www4.sii.cl/consdcvinternetui/#/bienvenida"
    SII_CLAVE_UNICA = "https://www4.sii.cl/consdcvinternetui/#/bienvenida"
    SII_F29_URL = "https://www4.sii.cl/propuestaf29ui/index.html#/default"
    
    def __init__(
        self,
        headless: bool = True,
        *,
        artifact_dir: Optional[Path] = None,
        run_id: Optional[str] = None,
    ):
        """
        Inicializa el cliente del SII.
        
        Args:
            headless: Si es True, el navegador se ejecutará en modo sin cabeza (headless).
            artifact_dir: Carpeta base para artefactos (capturas/HTML). Por defecto: output/
            run_id: Identificador de ejecución para agrupar capturas.
        """
        self.headless = headless
        self.driver = None
        self.is_authenticated = False
        self.current_period = None
        self.current_period_display = None
        self.period_already_declared = False
        self._period_declared_logged = False
        self.artifact_dir = Path(artifact_dir) if artifact_dir else Path("output")
        self.run_id = run_id or datetime.now().strftime("%Y%m%d_%H%M%S")
        self.screenshot_dir = self.artifact_dir / "screenshots" / self.run_id
        self.last_period_declared_screenshot: Optional[str] = None
        
    def start_browser(self):
        """Inicializa el navegador Selenium."""
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager
        from selenium.webdriver.chrome.options import Options
        
        chrome_options = Options()
        if self.headless:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        
        try:
            self.driver = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()),
                options=chrome_options
            )
            self.driver.implicitly_wait(10)
            return True
        except Exception as e:
            raise SIIConnectionError(f"Error al iniciar el navegador: {str(e)}")
    
    def _wait_for_first(self, selectors, description: str, wait_condition=None, timeout: int = 15):
        """
        Intenta encontrar el primer elemento que coincida con alguno de los selectores.
        
        Args:
            selectors: Lista de tuplas (By, selector)
            description: Descripción para mensajes de error
            wait_condition: Condición de Selenium (defaults to presence_of_element_located)
            timeout: Tiempo máximo de espera en segundos
        """
        wait_condition = wait_condition or EC.presence_of_element_located
        last_exc: Optional[Exception] = None
        for by, value in selectors:
            try:
                return WebDriverWait(self.driver, timeout).until(
                    wait_condition((by, value))
                )
            except TimeoutException as exc:
                last_exc = exc
                continue
        raise TimeoutException(f"No se encontró {description}") from last_exc
    
    def _click_first(self, selectors, description: str, timeout: int = 15):
        """Hace clic en el primer elemento disponible según los selectores proporcionados."""
        element = self._wait_for_first(
            selectors=selectors,
            description=description,
            wait_condition=EC.element_to_be_clickable,
            timeout=timeout
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(0.3)
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(1.2)
        return element

    def _save_screenshot(self, filename: str) -> str:
        """Guarda capturas en una carpeta por ejecución."""
        if not self.driver:
            return ""
        self.screenshot_dir.mkdir(parents=True, exist_ok=True)
        path = self.screenshot_dir / filename
        self.driver.save_screenshot(str(path))
        return str(path)

    def _log_period_declared(self, message: str) -> None:
        """Evita mensajes duplicados cuando el período ya está declarado."""
        if self._period_declared_logged:
            return
        print(message)
        self._period_declared_logged = True
    
    def _period_already_declared(self) -> bool:
        """
        Detecta si el SII muestra la pantalla de período ya declarado.
        
        Returns:
            bool: True si se detecta que el período ya está declarado
        """
        try:
            def normalize_text(value: str) -> str:
                normalized = unicodedata.normalize("NFKD", value or "")
                stripped = "".join(ch for ch in normalized if not unicodedata.combining(ch))
                return " ".join(stripped.lower().split())

            self.period_already_declared = False
            # Tomar captura de pantalla para depuración
            self._save_screenshot("sii_f29_debug_period_check.png")
            
            # Obtener todo el texto de la página en minúsculas
            page_text = normalize_text(self.driver.find_element(By.TAG_NAME, "body").text)
            
            # Lista de frases que indican que el período ya está declarado
            frases_declarado = [
                'ya existe una declaración',
                'declaración vigente para este período',
                'declaración vigente para este periodo',
                'declaración vigente para este período tributario',
                'declaración vigente para este periodo tributario',
                'existe una declaración vigente para este período tributario',
                'existe una declaración vigente para este periodo tributario',
                'ya existe una propuesta de declaración',
                'ya se encuentra una declaración',
                'ya existe una declaración vigente',
                'existe una declaración vigente',
                'no es posible presentar más de una declaración',
                'ya ha sido declarado',
                'periodo ya declarado',
                'ya existe declaración',
                'declaración existente',
                'ya fue declarado',
                'ya ha sido presentada',
                'ya se presentó',
                'ya se ha presentado',
                'ya se encuentra presentada',
                'ya se encuentra declarada',
                'ya ha sido declarada',
                'ya existe una declaración vigente para el período',
                'ya existe una declaración para el período',
                'ya existe una declaración del período',
                'ya existe declaración del período',
                'ya existe declaración para el período',
                'ya existe declaración vigente',
                'ya existe declaración vigente para el período',
                'el período ya ha sido declarado',
                'el período ya fue declarado',
                'el período ya se encuentra declarado',
                'el período ya ha sido presentado',
                'el período ya fue presentado',
                'el período ya se encuentra presentado',
                'consultar estado de declaración',
            ]
            frases_declarado_norm = [normalize_text(frase) for frase in frases_declarado]
            
            # Verificar si alguna de las frases está en el texto de la página
            for frase in frases_declarado_norm:
                if frase in page_text:
                    self._log_period_declared(
                        f"  ✅ Se detectó que el período ya tiene una declaración existente (frase: '{frase}')"
                    )
                    self.last_period_declared_screenshot = self._save_screenshot(
                        "sii_f29_periodo_ya_declarado.png"
                    )
                    self.period_already_declared = True
                    return True
            
            # Verificar también en el HTML completo por si acaso
            page_source = normalize_text(self.driver.page_source)
            for frase in frases_declarado_norm:
                if frase in page_source:
                    self._log_period_declared(
                        f"  ✅ [HTML] Se detectó que el período ya tiene una declaración existente (frase: '{frase}')"
                    )
                    self.last_period_declared_screenshot = self._save_screenshot(
                        "sii_f29_periodo_ya_declarado.png"
                    )
                    self.period_already_declared = True
                    return True
                    
            # Verificar elementos específicos que podrían indicar que ya está declarado
            try:
                # Buscar elementos que contengan texto de error o mensaje
                mensajes = self.driver.find_elements(
                    By.XPATH, 
                    '//*[contains(translate(., "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "declaración")] | ' +
                    '//*[contains(translate(., "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "periodo")] | ' +
                    '//*[contains(translate(., "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "vigente")]'
                )
                
                for elemento in mensajes:
                    texto = normalize_text(elemento.text)
                    if any(frase in texto for frase in frases_declarado_norm):
                        self._log_period_declared(
                            "  ✅ [Elemento] Se detectó que el período ya tiene una declaración existente"
                        )
                        self.last_period_declared_screenshot = self._save_screenshot(
                            "sii_f29_periodo_ya_declarado.png"
                        )
                        self.period_already_declared = True
                        return True
            except:
                pass
                
            return False
            
        except Exception as e:
            print(f"  ⚠️  Error al verificar si el período está declarado: {str(e)}")
            return False
    
    def login_with_clave_unica(self, rut: str, password: str) -> bool:
        """
        Inicia sesión en el SII usando ClaveÚnica.
        
        Args:
            rut: RUT del contribuyente (formato: 12345678-9)
            password: Contraseña de ClaveÚnica
            
        Returns:
            bool: True si la autenticación fue exitosa, False en caso contrario.
        """
        if not self.driver:
            self.start_browser()
            
        try:
            print(f"  - Navegando a {self.SII_PORTAL}...")
            self.driver.get(self.SII_PORTAL)
            
            # Esperar a que cargue la página de inicio de sesión
            print("  - Buscando botón de ClaveÚnica...")
            try:
                # Intentar encontrar el botón de ClaveÚnica
                clave_unica_btn = WebDriverWait(self.driver, 15).until(
                    EC.element_to_be_clickable((By.ID, "claveunica"))
                )
                print("  - Haciendo clic en el botón de ClaveÚnica...")
                clave_unica_btn.click()
                
                # Tomar captura de pantalla para depuración
                self._save_screenshot("sii_login_page.png")
                print("  - Captura de pantalla guardada como 'sii_login_page.png'")
                
                # Esperar a que cargue la página de ClaveÚnica
                print("  - Esperando a que cargue la página de ClaveÚnica...")
                WebDriverWait(self.driver, 15).until(
                    EC.presence_of_element_located((By.NAME, "_rutdocumento"))
                )
                
                # Rellenar formulario de ClaveÚnica
                print("  - Rellenando formulario de ClaveÚnica...")
                rut_input = self.driver.find_element(By.NAME, "_rutdocumento")
                rut_input.clear()
                rut_input.send_keys(rut.split('-')[0])  # Solo el número sin DV
                
                # Tomar otra captura de pantalla
                self._save_screenshot("sii_claveunica_form.png")
                
                print("\n  ⚠️  Autenticación manual requerida ⚠️")
                print("  Por favor, completa el proceso de autenticación en la ventana del navegador.")
                print("  Una vez que hayas iniciado sesión, podrás continuar.")
                print("  El script esperará hasta que la autenticación sea exitosa o se cancele.")
                
                # Esperar a que el usuario complete la autenticación manualmente
                input("  Presiona Enter cuando hayas completado la autenticación...")
                
                # Verificar si la autenticación fue exitosa
                if "bienvenido" in self.driver.current_url.lower() or "inicio" in self.driver.current_url.lower():
                    print("  ✅ Autenticación exitosa detectada")
                    self.is_authenticated = True
                    return True
                else:
                    print("  ⚠️  No se pudo verificar la autenticación automáticamente")
                    return False
                
            except TimeoutException as te:
                print(f"  ❌ Tiempo de espera agotado: {str(te)}")
                self._save_screenshot("sii_timeout_error.png")
                print("  Se guardó una captura de pantalla del error como 'sii_timeout_error.png'")
                return False
                
        except Exception as e:
            error_msg = f"Error durante la autenticación: {str(e)}"
            print(f"  ❌ {error_msg}")
            self._save_screenshot("sii_auth_error.png")
            print("  Se guardó una captura de pantalla del error como 'sii_auth_error.png'")
            raise SIIConnectionError(error_msg) from e
    
    def navigate_to_f29_no_movement(self, periodo: Optional[str] = None) -> bool:
        """
        Navega hasta el formulario F29 de declaración sin movimiento.
        
        Args:
            periodo: Período en formato YYYY-MM (ej: '2025-12'). Si es None, se usa el mes anterior.
            
        Returns:
            bool: True si se navegó correctamente, False si el período ya está declarado o hubo un error.
        """
        """
        Navega dentro del portal del SII hasta el formulario de Declaración F29 sin movimiento.
        
        Returns:
            bool: True si el formulario fue cargado correctamente.
        """
        if not self.driver:
            raise SIIConnectionError("El navegador no está inicializado.")
        
        if not self.is_authenticated:
            print("⚠️  Advertencia: no se ha detectado autenticación previa. Intentaré continuar.")
        
        print("  - Abriendo portal F29...")
        try:
            self.driver.get(self.SII_F29_URL)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            self._save_screenshot("sii_f29_step1.png")
            
            # Verificar si ya estamos en una pantalla de error o de período ya declarado
            time.sleep(1)  # Pequeña pausa para asegurar que la página cargue completamente
            if self._period_already_declared():
                self._log_period_declared("  ✅ El período ya tiene una declaración existente.")
                return False
                
        except Exception as e:
            print(f"  ⚠️  Error al cargar el portal F29: {str(e)}")
            self._save_screenshot("sii_f29_error_carga.png")
            return False
        
        meses = [
            "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
        ]
        if periodo:
            anio_obj, mes_obj = periodo.split("-")
            mes_idx = int(mes_obj)
            anio = int(anio_obj)
        else:
            hoy = datetime.now()
            mes_idx = hoy.month - 1
            anio = hoy.year
            if mes_idx == 0:
                mes_idx = 12
                anio -= 1
        mes_visible = meses[mes_idx - 1]
        self.current_period = f"{anio}-{mes_idx:02d}"
        self.current_period_display = f"{mes_visible} {anio}"
        
        print(f"  - Seleccionando período: {mes_visible} {anio}")
        # Obtener todos los selects disponibles con un pequeño retraso
        time.sleep(1)  # Pequeña pausa para asegurar que la página esté lista
        selects = self.driver.find_elements(By.TAG_NAME, 'select')
        
        if len(selects) >= 2:
            # Manejar mes
            select_mes = Select(selects[0])
            mes_actual = select_mes.first_selected_option.text.strip()
            if mes_actual != mes_visible:
                print(f"  - Ajustando mes de '{mes_actual}' a '{mes_visible}'")
                select_mes.select_by_visible_text(mes_visible)
                time.sleep(0.5)  # Pequeña pausa después de cambiar el mes
            else:
                print(f"  - Mes ya está configurado en {mes_visible}")
            
            # Manejar año
            select_anio = Select(selects[1])
            anio_actual = select_anio.first_selected_option.text.strip()
            if anio_actual != str(anio):
                print(f"  - Ajustando año de '{anio_actual}' a '{anio}'")
                select_anio.select_by_visible_text(str(anio))
                time.sleep(0.5)  # Pequeña pausa después de cambiar el año
            else:
                print(f"  - Año ya está configurado en {anio}")
            
            # Confirmar selección
            print("  - Confirmando período...")
            max_intentos = 3
            for intento in range(1, max_intentos + 1):
                try:
                    # Verificar si ya hay un mensaje de período declarado
                    if self._period_already_declared():
                        self._log_period_declared("  ✅ El período ya tiene una declaración existente.")
                        return False
                    
                    # Intentar encontrar y hacer clic en Aceptar
                    print(f"  - Haciendo clic en el botón de confirmación (intento {intento}/{max_intentos})...")
                    self._click_first(
                        selectors=[
                            (By.XPATH, "//button[contains(., 'Aceptar')]"),
                            (By.XPATH, "//button[contains(., 'Continuar')]"),
                            (By.XPATH, "//input[@type='submit' and contains(@value, 'Aceptar')]"),
                            (By.XPATH, "//input[@type='submit' and contains(@value, 'Continuar')]"),
                            (By.XPATH, "//a[contains(., 'Aceptar')]"),
                            (By.XPATH, "//a[contains(., 'Continuar')]"),
                        ],
                        description="botón de confirmación",
                        timeout=3,
                    )
                    time.sleep(1.5)  # Esperar a que se procese la acción
                    
                    # Verificar si apareció algún mensaje de error después de hacer clic
                    if self._period_already_declared():
                        self._log_period_declared(
                            "  ✅ El período ya tiene una declaración existente (después de confirmar)."
                        )
                        return False
                        
                    # Si llegamos aquí, el clic fue exitoso
                    break
                    
                except Exception as e:
                    if intento == max_intentos:
                        print(f"  ⚠️  No se pudo confirmar el período después de {max_intentos} intentos: {str(e)}")
                        print("  ℹ️  Continuando de todos modos...")
                    else:
                        print(f"  ⚠️  Intento {intento} fallido, reintentando...")
                        time.sleep(1)
        else:
            print("  ⚠️  No se encontraron los selectores de mes/año, continuando...")
        
        print("  - Esperando pantalla de declaración...")
        time.sleep(2)  # Dar tiempo a que cargue la siguiente pantalla
        
        # Tomar captura de pantalla para depuración
        self._save_screenshot("sii_f29_antes_verificar_declarado.png")
        
        # Verificar si el período ya está declarado (con múltiples intentos)
        for intento in range(1, 4):
            if self._period_already_declared():
                self._log_period_declared("  ✅ El SII indica que ya existe una declaración para este período.")
                print("  🏁 Proceso finalizado: No es necesario realizar acciones adicionales.")
                return False
            
            if intento < 3:
                print(f"  ⏳ Verificando estado del período (intento {intento + 1}/3)...")
                time.sleep(1)  # Pequeña pausa entre intentos
        
        # Si llegamos aquí, no se detectó que el período esté declarado
        print("  ℹ️  No se detectó que el período esté declarado, continuando...")
        
        try:
            # Intentar encontrar el botón de Sin Movimiento con un timeout mayor
            print("  - Buscando opción 'Sin movimiento'...")
            
            # Primero intentar con un selector más específico
            try:
                sin_mov_btn = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((
                        By.XPATH, 
                        "//button[contains(translate(., 'SINMOVIMIENTO', 'sinmovimiento'), 'sin movimiento')] | "
                        "//a[contains(translate(., 'SINMOVIMIENTO', 'sinmovimiento'), 'sin movimiento')]"
                    ))
                )
            except:
                # Si falla, intentar con un selector más genérico
                print("  - No se encontró el botón con selector específico, intentando con uno más genérico...")
                sin_mov_btn = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((
                        By.XPATH, 
                        "//*[contains(translate(., 'SINMOVIMIENTO', 'sinmovimiento'), 'sin movimiento')]"
                    ))
                )
            
            print("  - Haciendo clic en 'Sin movimiento'...")
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'}); arguments[0].click();", sin_mov_btn)
            
            # Esperar a que se complete la acción
            time.sleep(1.5)
            
            # Tomar captura después de la acción
            self._save_screenshot("sii_f29_despues_click_sin_movimiento.png")
            
            # Verificar si apareció algún mensaje de error o confirmación
            if self._period_already_declared():
                self._log_period_declared("  ✅ El SII indica que ya existe una declaración para este período.")
                print("  🏁 Proceso finalizado: No es necesario realizar acciones adicionales.")
                return False
                
            print("  - Modal de Sin Movimiento confirmado.")
            return True
            
        except TimeoutException:
            # Si hay un timeout, verificar si es porque ya está declarado
            if self._period_already_declared():
                self._log_period_declared("  ✅ El SII indica que ya existe una declaración para este período.")
                print("  🏁 Proceso finalizado: No es necesario realizar acciones adicionales.")
                return False
                
            # Si no es por período declarado, verificar si estamos en la pantalla final
            page_source = self.driver.page_source.lower()
            if "enviar" in page_source or "declaración" in page_source or "continuar" in page_source:
                print("  ℹ️  No se encontró el botón 'Sin movimiento', pero parece que ya estamos en la pantalla de declaración")
                return True
                
            # Si no es ninguno de los casos anteriores, mostrar error
            self._save_screenshot("sii_f29_error.png")
            print("  ⚠️  No se pudo encontrar la opción 'Sin movimiento' en la página")
            print("  ℹ️  Se ha guardado una captura de pantalla en 'sii_f29_error.png'")
            
            # A pesar del error, intentar continuar si parece que estamos en una pantalla de declaración
            if any(x in page_source for x in ["declaración", "enviar", "continuar"]):
                print("  ℹ️  Continuando ya que parece que estamos en una pantalla de declaración...")
                return True
                
            return False
    
    def submit_f29_no_movement(self, download_dir: Optional[Path] = None) -> Optional[Dict[str, Optional[str]]]:
        """
        Envía la declaración sin movimiento y captura el comprobante.
        
        Returns:
            dict con información del envío (folio, ruta de captura, etc.) o None si ya está declarado.
        """
        if not self.driver:
            raise SIIConnectionError("El navegador no está inicializado.")
        
        # Tomar captura de la pantalla actual para depuración
        self._save_screenshot("sii_f29_antes_de_enviar.png")
        
        # Verificar primero si el período ya está declarado (con múltiples intentos)
        for intento in range(1, 4):
            if self._period_already_declared():
                self._log_period_declared("  ✅ El período ya tiene una declaración vigente.")
                print("  🏁 Para rectificar, dirígete a 'Consultar estado de declaración'.")
                return {
                    'estado': 'ya_declarado',
                    'mensaje': 'El período ya tiene una declaración vigente',
                    'screenshot': self.last_period_declared_screenshot
                }
            if intento < 3:
                print(f"  ⏳ Verificando estado del período (intento {intento + 1}/3)...")
                time.sleep(1)
        
        print("  - Intentando enviar declaración sin movimiento...")
        
        try:
            # Intentar encontrar el botón de enviar con varios selectores
            try:
                self._click_first(
                    selectors=[
                        (By.XPATH, "//button[contains(., 'Enviar')]"),
                        (By.XPATH, "//a[contains(., 'Enviar')]"),
                        (By.XPATH, "//*[contains(translate(., 'ENVIAR', 'enviar'), 'enviar')]"),
                        (By.XPATH, "//button[contains(., 'Presentar')]"),
                        (By.XPATH, "//a[contains(., 'Presentar')]"),
                        (By.XPATH, "//input[@type='submit' and contains(@value, 'Enviar')]"),
                        (By.XPATH, "//input[@type='submit' and contains(@value, 'Presentar')]"),
                    ],
                    description="botón de enviar",
                    timeout=8,
                )
                print("  - Haciendo clic en el botón de enviar...")
                time.sleep(2)  # Esperar a que se procese el clic
            except TimeoutException:
                print("  ⚠️  No se pudo encontrar el botón de enviar, verificando estado...")
                if self._period_already_declared():
                    self._log_period_declared("  ✅ El período ya tiene una declaración vigente.")
                    print("  🏁 Para rectificar, dirígete a 'Consultar estado de declaración'.")
                    return {
                        'estado': 'ya_declarado',
                        'mensaje': 'El período ya tiene una declaración vigente',
                        'screenshot': self.last_period_declared_screenshot
                    }
                raise
            
            # Esperar confirmación del envío
            print("  - Esperando confirmación del SII...")
            
            # Tomar captura después de hacer clic en enviar
            self._save_screenshot("sii_f29_despues_de_enviar.png")
            
            # Verificar si el período ya está declarado después de hacer clic
            if self._period_already_declared():
                self._log_period_declared("  ✅ El período ya tiene una declaración vigente.")
                print("  🏁 Para rectificar, dirígete a 'Consultar estado de declaración'.")
                return {
                    'estado': 'ya_declarado',
                    'mensaje': 'El período ya tiene una declaración vigente',
                    'screenshot': self.last_period_declared_screenshot
                }
            
            # Esperar mensaje de confirmación
            try:
                confirm_element = self._wait_for_first(
                    selectors=[
                        (By.XPATH, "//*[contains(., 'Certificado de Recepción')]"),
                        (By.XPATH, "//*[contains(., 'Declaración ingresada')]"),
                        (By.XPATH, "//*[contains(., 'Número de control')]"),
                        (By.XPATH, "//*[contains(., 'existe una declaración vigente')]"),
                        (By.XPATH, "//*[contains(., 'su declaración ha sido ingresada')]"),
                        (By.XPATH, "//*[contains(., 'su declaración fue ingresada')]"),
                        (By.XPATH, "//*[contains(., 'su declaración se ha ingresado')]"),
                        (By.XPATH, "//*[contains(., 'ha sido recibida satisfactoriamente')]"),
                        (By.XPATH, "//*[contains(., 'ha sido recibida exitosamente')]"),
                    ],
                    description="mensaje de confirmación",
                    wait_condition=EC.presence_of_element_located,
                    timeout=15,
                )
                
                # Tomar captura de la confirmación
                confirm_screenshot = self._save_screenshot("sii_f29_confirmacion.png")
                
                # Verificar si el mensaje es de confirmación o de error
                confirm_text = confirm_element.text.lower()
                if any(phrase in confirm_text for phrase in ['certificado', 'ingresada', 'recibida', 'éxito', 'exito', 'satisfactoriamente']):
                    print("  ✅ Declaración enviada exitosamente")
                    return {
                        'estado': 'enviado',
                        'mensaje': 'Declaración enviada exitosamente',
                        'screenshot': confirm_screenshot,
                        'fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    }
                else:
                    print(f"  ⚠️  Se recibió un mensaje inesperado: {confirm_text[:100]}...")
                    return {
                        'estado': 'advertencia',
                        'mensaje': 'Se recibió un mensaje inesperado',
                        'detalle': confirm_text[:500],
                        'screenshot': confirm_screenshot
                    }
                    
            except TimeoutException:
                # Si hay timeout, verificar si es porque el período ya está declarado
                if self._period_already_declared():
                    self._log_period_declared("  ✅ El período ya tiene una declaración vigente.")
                    print("  🏁 Para rectificar, dirígete a 'Consultar estado de declaración'.")
                    return {
                        'estado': 'ya_declarado',
                        'mensaje': 'El período ya tiene una declaración vigente',
                        'screenshot': self.last_period_declared_screenshot
                    }
                
                # Si no es por período declarado, guardar captura y lanzar error
                error_screenshot = self._save_screenshot("sii_f29_error_confirmacion.png")
                print("  ❌ No se pudo confirmar el envío de la declaración")
                print("  ℹ️  Se ha guardado una captura de pantalla en 'sii_f29_error_confirmacion.png'")
                
                # Verificar si hay algún mensaje de error visible
                try:
                    mensajes_error = self.driver.find_elements(By.CSS_SELECTOR, ".alert-danger, .error, .mensaje-error, .alert.alert-danger")
                    if mensajes_error:
                        error_text = " | ".join([msg.text for msg in mensajes_error if msg.text.strip()])
                        print(f"  ❌ Mensaje de error: {error_text[:200]}...")
                        return {
                            'estado': 'error',
                            'mensaje': 'Error al enviar la declaración',
                            'detalle': error_text[:500],
                            'screenshot': error_screenshot
                        }
                except:
                    pass
                    
                raise SIIConnectionError("No se recibió confirmación del SII después de enviar la declaración.")
                
        except Exception as e:
            # Manejar cualquier otro error inesperado
            error_screenshot = self._save_screenshot("sii_f29_error_inesperado.png")
            print(f"  ❌ Error inesperado: {str(e)}")
            print("  ℹ️  Se ha guardado una captura de pantalla en 'sii_f29_error_inesperado.png'")
            
            # Verificar si el error fue porque el período ya está declarado
            if self._period_already_declared():
                self._log_period_declared("  ✅ El período ya tiene una declaración vigente.")
                print("  🏁 Para rectificar, dirígete a 'Consultar estado de declaración'.")
                return {
                    'estado': 'ya_declarado',
                    'mensaje': 'El período ya tiene una declaración vigente',
                    'screenshot': self.last_period_declared_screenshot
                }
                
            # Si no es por período declarado, relanzar la excepción
            raise
        
        download_dir = download_dir or Path("output")
        download_dir.mkdir(parents=True, exist_ok=True)
        periodo = self.current_period or datetime.now().strftime("%Y-%m")
        screenshot_path = download_dir / f"f29_sin_mov_{periodo}_confirmacion.png"
        html_path = download_dir / f"f29_sin_mov_{periodo}_confirmacion.html"
        self.driver.save_screenshot(str(screenshot_path))
        html_path.write_text(self.driver.page_source, encoding="utf-8")
        print(f"  - Confirmación capturada en {screenshot_path}")
        
        folio = None
        try:
            folio_el = self.driver.find_element(
                By.XPATH,
                "//*[contains(text(),'Folio') or contains(text(),'Número de control') or contains(text(),'Nº de folio')]"
            )
            folio = folio_el.text.strip()
        except NoSuchElementException:
            pass
        
        try:
            certificado_link = self.driver.find_element(
                By.XPATH,
                "//a[contains(., 'Certificado') or contains(., 'Descargar') or contains(., 'Imprimir')]"
            )
            certificado_href = certificado_link.get_attribute("href")
        except NoSuchElementException:
            certificado_href = None
        
        return {
            "periodo": periodo,
            "folio": folio,
            "screenshot": str(screenshot_path),
            "html": str(html_path),
            "certificado_href": certificado_href,
        }
    
    def login_with_rut_password(self, rut: str, password: str) -> bool:
        """
        Inicia sesión en el SII usando RUT y contraseña (método tradicional).
        
        Args:
            rut: RUT del contribuyente (formato: 12345678-9)
            password: Contraseña del SII
            
        Returns:
            bool: True si la autenticación fue exitosa, False en caso contrario.
        """
        if not self.driver:
            self.start_browser()
        
        try:
            print(f"  - Navegando a {self.SII_PORTAL}...")
            self.driver.get(self.SII_PORTAL)
            self._save_screenshot("sii_initial_page.png")
            print("  - Captura de pantalla inicial guardada como 'sii_initial_page.png'")
            
            print("  - Esperando a que cargue el formulario de acceso...")
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            self._save_screenshot("sii_page_loaded.png")
            
            # Algunos formularios están dentro de iframes
            try:
                iframe = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.TAG_NAME, "iframe"))
                )
                self.driver.switch_to.frame(iframe)
                print("  - Cambiando al iframe del formulario...")
            except TimeoutException:
                print("  - No se detectó iframe, continuando en el DOM principal.")
            
            rut_input = self._wait_for_first(
                selectors=[
                    (By.NAME, "rutcntr"),
                    (By.ID, "rutcntr"),
                    (By.NAME, "rut"),
                    (By.ID, "rut"),
                ],
                description="campo de RUT",
            )
            
            password_input = self._wait_for_first(
                selectors=[
                    (By.NAME, "clave"),
                    (By.ID, "clave"),
                    (By.NAME, "password"),
                    (By.ID, "password"),
                ],
                description="campo de contraseña",
            )
            
            login_button = self._wait_for_first(
                selectors=[
                    (By.XPATH, "//button[contains(., 'Ingresar')]"),
                    (By.XPATH, "//input[@type='submit' or @value='Ingresar']"),
                ],
                description="botón de ingreso",
                wait_condition=EC.element_to_be_clickable,
            )
            
            print("  - Completando formulario de autenticación...")
            rut_input.clear()
            rut_input.send_keys(rut.upper())
            password_input.clear()
            password_input.send_keys(password)
            self._save_screenshot("sii_before_login.png")
            
            print("  - Enviando formulario...")
            self.driver.execute_script("arguments[0].click();", login_button)
            
            self.driver.switch_to.default_content()
            print("  - Esperando confirmación de acceso...")
            WebDriverWait(self.driver, 20).until(
                lambda drv: any(
                    token in drv.current_url.lower()
                    for token in ("bienvenida", "inicio", "portal", "consdcvinternet")
                )
            )
            self._save_screenshot("sii_after_login.png")
            print("  ✅ Inicio de sesión detectado (URL actual:", self.driver.current_url, ")")
            self.is_authenticated = True
            return True
        
        except TimeoutException as te:
            print(f"  ❌ Tiempo de espera agotado: {str(te)}")
            self._save_screenshot("sii_timeout_error.png")
            print("  Se guardó una captura de pantalla del error como 'sii_timeout_error.png'")
            return False
        except Exception as e:
            error_msg = f"Error durante el inicio de sesión: {str(e)}"
            print(f"  ❌ {error_msg}")
            self._save_screenshot("sii_login_error.png")
            print("  Se guardó una captura de pantalla del error como 'sii_login_error.png'")
            raise SIIConnectionError(error_msg) from e
    
    def close(self):
        """Cierra el navegador y libera recursos."""
        if self.driver:
            self.driver.quit()
            self.driver = None
            self.is_authenticated = False
    
    def __enter__(self):
        """Permite usar la clase con el patrón 'with'."""
        self.start_browser()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Asegura que el navegador se cierre correctamente."""
        self.close()

