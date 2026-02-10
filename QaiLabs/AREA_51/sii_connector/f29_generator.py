"""
Módulo para generar declaraciones de IVA (F29) para el SII de Chile.

Este módulo permite generar declaraciones de IVA, tanto para casos sin movimiento
como con movimientos, siguiendo el formato requerido por el SII.
"""

import os
import json
from copy import deepcopy
from datetime import datetime
from typing import Dict, List, Optional, Union
from pathlib import Path

# Constantes
F29_TEMPLATE = {
    "encabezado": {
        "tipo_operacion": "VENTA",
        "tipo_servicio": "1",  # 1: Primera categoría, 2: Segunda categoría
        "tipo_entrega": "1",   # 1: Electrónica, 2: En papel
        "fecha_resolucion": "",
        "numero_resolucion": "",
        "periodo_tributario": "",  # Formato: AAAA-MM
        "fecha_vencimiento": "",
    },
    "identificacion": {
        "rut_emisor": "",
        "dv_emisor": "",
        "razon_social": "",
        "giro": "",
        "comuna": "",
        "direccion": "",
    },
    "resumen_operaciones": {
        "total_afecto": 0,
        "total_exento": 0,
        "total_iva": 0,
        "total_credito_iva": 0,
        "total_debito_iva": 0,
        "iva_retenido": 0,
        "iva_utilizado": 0,
        "iva_pagado": 0,
        "iva_por_pagar": 0,
    },
    "detalle_operaciones": [],
    "firma": {
        "fecha_firma": "",
        "firma_electronica": "",
    },
}

class F29Generator:
    """Clase para generar declaraciones de IVA (F29)."""
    
    def __init__(self, rut_empresa: str, periodo_tributario: str):
        """
        Inicializa el generador de F29.
        
        Args:
            rut_empresa: RUT de la empresa (formato: 12345678-9)
            periodo_tributario: Período tributario en formato AAAA-MM
        """
        self.rut_empresa = rut_empresa
        self.periodo_tributario = periodo_tributario
        self.declaracion = deepcopy(F29_TEMPLATE)
        self._inicializar_declaracion()
    
    def _inicializar_declaracion(self):
        """Inicializa la declaración con valores por defecto."""
        # Configurar período tributario
        self.declaracion["encabezado"]["periodo_tributario"] = self.periodo_tributario
        
        # Configurar fechas
        hoy = datetime.now().strftime("%Y-%m-%d")
        self.declaracion["encabezado"]["fecha_resolucion"] = hoy
        
        # Calcular fecha de vencimiento (último día del mes siguiente al período)
        anio, mes = map(int, self.periodo_tributario.split('-'))
        if mes == 12:
            anio += 1
            mes = 1
        else:
            mes += 1
        from calendar import monthrange
        ultimo_dia = monthrange(anio, mes)[1]
        self.declaracion["encabezado"]["fecha_vencimiento"] = f"{anio}-{mes:02d}-{ultimo_dia}"
        
        # Configurar firma
        self.declaracion["firma"]["fecha_firma"] = hoy
    
    def generar_sin_movimiento(self) -> Dict:
        """
        Genera una declaración de IVA sin movimiento.
        
        Returns:
            dict: Declaración de IVA sin movimiento en formato JSON.
        """
        # Configurar resumen para declaración sin movimiento
        self.declaracion["resumen_operaciones"].update({
            "total_afecto": 0,
            "total_exento": 0,
            "total_iva": 0,
            "total_credito_iva": 0,
            "total_debito_iva": 0,
            "iva_retenido": 0,
            "iva_utilizado": 0,
            "iva_pagado": 0,
            "iva_por_pagar": 0,
        })
        
        # Limpiar detalle de operaciones
        self.declaracion["detalle_operaciones"] = []
        
        return self.declaracion

    def set_identificacion(
        self,
        rut_emisor: Optional[str] = None,
        dv_emisor: Optional[str] = None,
        razon_social: Optional[str] = None,
        giro: Optional[str] = None,
        comuna: Optional[str] = None,
        direccion: Optional[str] = None,
    ) -> None:
        """Actualiza los datos de identificación de la declaración."""
        identificacion = self.declaracion["identificacion"]
        if rut_emisor is not None:
            identificacion["rut_emisor"] = rut_emisor
        if dv_emisor is not None:
            identificacion["dv_emisor"] = dv_emisor
        if razon_social is not None:
            identificacion["razon_social"] = razon_social
        if giro is not None:
            identificacion["giro"] = giro
        if comuna is not None:
            identificacion["comuna"] = comuna
        if direccion is not None:
            identificacion["direccion"] = direccion
    
    def agregar_operacion(
        self,
        tipo_documento: int,
        fecha_emision: str,
        numero_documento: str,
        rut_emisor: str,
        monto_afecto: float,
        monto_exento: float,
        iva: float,
        tipo_operacion: str = "VENTA"
    ) -> None:
        """
        Agrega una operación a la declaración.
        
        Args:
            tipo_documento: Código de tipo de documento (33: Factura, 34: Factura exenta, etc.)
            fecha_emision: Fecha de emisión del documento (YYYY-MM-DD)
            numero_documento: Número del documento
            rut_emisor: RUT del emisor del documento (formato: 12345678-9)
            monto_afecto: Monto afecto a IVA
            monto_exento: Monto exento de IVA
            iva: Monto de IVA
            tipo_operacion: Tipo de operación (VENTA o COMPRA)
        """
        operacion = {
            "tipo_documento": tipo_documento,
            "fecha_emision": fecha_emision,
            "numero_documento": numero_documento,
            "rut_emisor": rut_emisor,
            "monto_afecto": monto_afecto,
            "monto_exento": monto_exento,
            "iva": iva,
            "tipo_operacion": tipo_operacion,
        }
        
        self.declaracion["detalle_operaciones"].append(operacion)
        
        # Actualizar resumen
        resumen = self.declaracion["resumen_operaciones"]
        resumen["total_afecto"] += monto_afecto
        resumen["total_exento"] += monto_exento
        resumen["total_iva"] += iva
        
        if tipo_operacion == "COMPRA":
            resumen["total_credito_iva"] += iva
        else:  # VENTA
            resumen["total_debito_iva"] += iva
        
        # Calcular IVA por pagar
        resumen["iva_por_pagar"] = resumen["total_debito_iva"] - resumen["total_credito_iva"] - resumen["iva_retenido"]
    
    def generar_json(self, ruta_archivo: str = None) -> Union[Dict, None]:
        """
        Genera un archivo JSON con la declaración.
        
        Args:
            ruta_archivo: Ruta donde se guardará el archivo JSON. Si es None, retorna el diccionario.
            
        Returns:
            dict: La declaración en formato JSON si ruta_archivo es None, None en caso contrario.
        """
        if ruta_archivo:
            with open(ruta_archivo, 'w', encoding='utf-8') as f:
                json.dump(self.declaracion, f, ensure_ascii=False, indent=2)
            return None
        return self.declaracion
    
    def generar_xml(self, ruta_archivo: str) -> bool:
        """
        Genera un archivo XML con la declaración (formato SII).
        
        Args:
            ruta_archivo: Ruta donde se guardará el archivo XML.
            
        Returns:
            bool: True si se generó correctamente, False en caso contrario.
        """
        # Implementación pendiente
        # Esto requerirá mapear la estructura JSON al formato XML del SII
        raise NotImplementedError("La generación de XML aún no está implementada.")

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una instancia del generador
    generador = F29Generator("12345678-9", "2026-01")
    
    # Generar declaración sin movimiento
    declaracion = generador.generar_sin_movimiento()
    
    # Guardar en un archivo JSON
    os.makedirs("output", exist_ok=True)
    ruta_json = "output/f29_sin_movimiento.json"
    generador.generar_json(ruta_json)
    print(f"Declaración generada: {ruta_json}")
    
    # Ejemplo con operaciones
    generador_con_movimientos = F29Generator("12345678-9", "2026-01")
    
    # Agregar algunas operaciones de ejemplo
    generador_con_movimientos.agregar_operacion(
        tipo_documento=33,  # Factura electrónica
        fecha_emision="2026-01-05",
        numero_documento="123",
        rut_emisor="7654321-0",
        monto_afecto=1000000,
        monto_exento=0,
        iva=190000,
        tipo_operacion="COMPRA"
    )
    
    generador_con_movimientos.agregar_operacion(
        tipo_documento=33,  # Factura electrónica
        fecha_emision="2026-01-10",
        numero_documento="456",
        rut_emisor="9876543-2",
        monto_afecto=2000000,
        monto_exento=0,
        iva=380000,
        tipo_operacion="VENTA"
    )
    
    # Guardar declaración con movimientos
    ruta_json_movimientos = "output/f29_con_movimientos.json"
    generador_con_movimientos.generar_json(ruta_json_movimientos)
    print(f"Declaración con movimientos generada: {ruta_json_movimientos}")
