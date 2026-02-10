# Mini-PRD: Módulo de Conciliación Bancaria Automática

## 1. Resumen del Problema
Los administradores pierden horas comparando manualmente la cartola bancaria (PDF/Excel) con los pagos registrados en el sistema. Es un proceso propenso a errores humanos que causa descuadres financieros y desconfianza en la comunidad.

## 2. Solución Propuesta
Un módulo que ingesta los movimientos bancarios y utiliza algoritmos de coincidencia (matching) para asociarlos automáticamente con los gastos comunes y otros ingresos esperados, requiriendo intervención humana solo para las excepciones.

## 3. Historias de Usuario Clave

### HU-01: Importación de Cartola
*   **Como** Administrador,
*   **Quiero** subir mi cartola bancaria en formato Excel o CSV (y a futuro conectar vía API),
*   **Para** que el sistema tenga los movimientos reales del banco sin tener que digitarlos uno a uno.

### HU-02: Conciliación Automática (The Magic)
*   **Como** Sistema,
*   **Quiero** comparar cada movimiento bancario con los cobros pendientes,
*   **Para** sugerir "matches" basados en: Monto exacto, RUT en glosa, o N° de Unidad en referencia.

### HU-03: Resolución de Conflictos
*   **Como** Administrador,
*   **Quiero** ver una interfaz clara de "Semáforo" (Verde: Calce perfecto, Amarillo: Posible coincidencia, Rojo: Sin coincidencia),
*   **Para** aprobar los verdes rápidamente y enfocarme solo en investigar los rojos.

## 4. Requerimientos Funcionales

### 4.1. Ingesta de Datos
*   Soporte inicial para formatos CSV y Excel estándar de bancos principales (Banco de Chile, Santander, Scotiabank).
*   Normalización de datos: Fecha, Descripción/Glosa, Monto (Cargo/Abono), Saldo.

### 4.2. Algoritmo de Matching
El sistema debe buscar coincidencias en el siguiente orden de prioridad:
1.  **Match Perfecto:** Monto exacto + Identificador único en glosa (ej. "DPTO 402").
2.  **Match por Monto y Fecha:** Monto exacto + Fecha cercana (+/- 3 días).
3.  **Match Parcial:** Monto similar (dentro de un rango de tolerancia pequeña) + Identificador.

### 4.3. Acciones de Conciliación
*   **Conciliar:** Marca el movimiento como "Conciliado" y genera el recibo de pago si no existía.
*   **Ignorar:** Para movimientos que no corresponden al sistema (ej. comisiones bancarias internas que se registran como gasto global).
*   **Crear Gasto/Ingreso:** Opción rápida para crear el registro contable desde el movimiento bancario si falta.

## 5. Requerimientos No Funcionales (UX/UI)
*   **Interfaz Dividida:** Pantalla partida. Izquierda: Movimientos Banco. Derecha: Registros Sistema. Líneas conectoras visuales para los matches.
*   **Feedback Inmediato:** Indicador de "% de Conciliación" que sube a medida que el usuario aprueba.

## 6. Métricas de Éxito (KPIs)
*   **Tasa de Auto-Conciliación:** % de movimientos que el sistema empareja correctamente sin ayuda. Meta inicial: >60%.
*   **Tiempo de Proceso:** Reducir el tiempo de conciliación mensual de 4 horas a 30 minutos.
