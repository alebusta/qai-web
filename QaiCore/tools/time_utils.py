"""
Utilidades de tiempo para agentes IA.
Permite a los agentes tener noción temporal y calcular prioridades basadas en fechas.
"""

from datetime import datetime, timedelta
from typing import Dict, List, Optional
import re


def get_current_datetime() -> Dict[str, str]:
    """
    Obtiene la fecha y hora actual en formato estructurado.
    
    Returns:
        Dict con fecha, hora, día de semana, etc.
    """
    now = datetime.now()
    
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    
    return {
        "timestamp": now.isoformat(),
        "fecha": now.strftime("%d-%b-%Y"),
        "fecha_corta": now.strftime("%d/%m/%Y"),
        "hora": now.strftime("%H:%M:%S"),
        "dia_semana": dias_semana[now.weekday()],
        "dia": now.day,
        "mes": meses[now.month - 1],
        "mes_num": now.month,
        "año": now.year,
        "es_fin_de_semana": now.weekday() >= 5
    }


def get_current_context() -> str:
    """
    Retorna una descripción en lenguaje natural del momento actual.
    Útil para que agentes mencionen el contexto temporal al usuario.
    
    Returns:
        String tipo: "Hoy es Jueves 26 de Diciembre de 2025, 13:15"
    """
    info = get_current_datetime()
    return f"Hoy es {info['dia_semana']} {info['dia']} de {info['mes']} de {info['año']}, {info['hora'][:5]}"


def parse_date_from_task(task_text: str) -> Optional[datetime]:
    """
    Intenta extraer una fecha de una tarea.
    
    Formatos soportados:
    - "hasta 15-Dic"
    - "para el 20/12"
    - "deadline: 2025-12-30"
    
    Args:
        task_text: Texto de la tarea
        
    Returns:
        datetime object o None si no encuentra fecha
    """
    # Patrones de fecha comunes
    patterns = [
        r'(\d{1,2})-([A-Za-z]{3})',  # 15-Dic
        r'(\d{1,2})/(\d{1,2})/(\d{2,4})',  # 15/12/25 o 15/12/2025
        r'(\d{4})-(\d{2})-(\d{2})',  # 2025-12-15
        r'(hasta|para|deadline).*?(\d{1,2})\s+de\s+([A-Za-z]+)',  # "hasta 15 de diciembre"
    ]
    
    meses_map = {
        'ene': 1, 'enero': 1, 'feb': 2, 'febrero': 2, 'mar': 3, 'marzo': 3,
        'abr': 4, 'abril': 4, 'may': 5, 'mayo': 5, 'jun': 6, 'junio': 6,
        'jul': 7, 'julio': 7, 'ago': 8, 'agosto': 8, 'sep': 9, 'septiembre': 9,
        'oct': 10, 'octubre': 10, 'nov': 11, 'noviembre': 11, 'dic': 12, 'diciembre': 12
    }
    
    # Intentar cada patrón
    task_lower = task_text.lower()
    
    # Patrón 1: 15-Dic
    match = re.search(r'(\d{1,2})-([a-z]{3})', task_lower)
    if match:
        dia = int(match.group(1))
        mes_str = match.group(2)
        mes = meses_map.get(mes_str)
        if mes:
            año_actual = datetime.now().year
            try:
                return datetime(año_actual, mes, dia)
            except ValueError:
                pass
    
    # Patrón 2: 15/12/2025 o 15/12
    match = re.search(r'(\d{1,2})/(\d{1,2})(?:/(\d{2,4}))?', task_text)
    if match:
        dia = int(match.group(1))
        mes = int(match.group(2))
        año = int(match.group(3)) if match.group(3) else datetime.now().year
        if año < 100:  # Convertir 25 → 2025
            año += 2000
        try:
            return datetime(año, mes, dia)
        except ValueError:
            pass
    
    # Patrón 3: 2025-12-15
    match = re.search(r'(\d{4})-(\d{2})-(\d{2})', task_text)
    if match:
        año = int(match.group(1))
        mes = int(match.group(2))
        dia = int(match.group(3))
        try:
            return datetime(año, mes, dia)
        except ValueError:
            pass
    
    return None


def calculate_task_urgency(task_text: str, deadline: Optional[datetime] = None) -> Dict:
    """
    Calcula la urgencia de una tarea basada en su deadline.
    
    Args:
        task_text: Texto de la tarea
        deadline: Fecha límite (opcional, se intenta extraer del texto si no se provee)
        
    Returns:
        Dict con nivel de urgencia, días restantes, etc.
    """
    if deadline is None:
        deadline = parse_date_from_task(task_text)
    
    if deadline is None:
        return {
            "urgency_level": "unknown",
            "urgency_text": "Sin fecha límite definida",
            "days_remaining": None,
            "is_overdue": False,
            "priority_score": 50  # Prioridad media por defecto
        }
    
    now = datetime.now()
    delta = deadline - now
    days_remaining = delta.days
    
    # Determinar nivel de urgencia
    if days_remaining < 0:
        urgency_level = "overdue"
        urgency_text = f"⚠️ ATRASADA ({abs(days_remaining)} días)"
        priority_score = 100
    elif days_remaining == 0:
        urgency_level = "today"
        urgency_text = "🔴 HOY"
        priority_score = 95
    elif days_remaining <= 2:
        urgency_level = "critical"
        urgency_text = f"🔴 URGENTE ({days_remaining} días)"
        priority_score = 90
    elif days_remaining <= 7:
        urgency_level = "high"
        urgency_text = f"🟠 Alta ({days_remaining} días)"
        priority_score = 70
    elif days_remaining <= 30:
        urgency_level = "medium"
        urgency_text = f"🟡 Media ({days_remaining} días)"
        priority_score = 40
    else:
        urgency_level = "low"
        urgency_text = f"🟢 Baja ({days_remaining} días)"
        priority_score = 20
    
    return {
        "urgency_level": urgency_level,
        "urgency_text": urgency_text,
        "days_remaining": days_remaining,
        "is_overdue": days_remaining < 0,
        "deadline": deadline.strftime("%d-%b-%Y"),
        "priority_score": priority_score
    }


def prioritize_tasks(tasks: List[str]) -> List[Dict]:
    """
    Ordena una lista de tareas por prioridad basada en urgencia.
    
    Args:
        tasks: Lista de strings con tareas
        
    Returns:
        Lista de dicts con tareas ordenadas por prioridad
    """
    task_analysis = []
    
    for task in tasks:
        urgency = calculate_task_urgency(task)
        task_analysis.append({
            "task": task,
            **urgency
        })
    
    # Ordenar por priority_score descendente
    task_analysis.sort(key=lambda x: x['priority_score'], reverse=True)
    
    return task_analysis


def format_task_with_urgency(task: str) -> str:
    """
    Formatea una tarea agregando indicador de urgencia visual.
    
    Args:
        task: Texto de la tarea
        
    Returns:
        Tarea formateada con indicador de urgencia
    """
    urgency = calculate_task_urgency(task)
    
    # Si ya tiene checkbox markdown, preservarlo
    checkbox_match = re.match(r'^(\s*-\s*\[[ x]\]\s*)', task)
    checkbox_prefix = checkbox_match.group(1) if checkbox_match else ""
    task_clean = task[len(checkbox_prefix):] if checkbox_prefix else task
    
    # Agregar indicador de urgencia
    if urgency['urgency_level'] != 'unknown':
        return f"{checkbox_prefix}[{urgency['urgency_text']}] {task_clean}"
    else:
        return task


# Ejemplo de uso
if __name__ == "__main__":
    print("="*60)
    print("CONTEXTO TEMPORAL ACTUAL")
    print("="*60)
    print(get_current_context())
    print()
    
    info = get_current_datetime()
    for key, value in info.items():
        print(f"{key}: {value}")
    
    print("\n" + "="*60)
    print("ANÁLISIS DE URGENCIA DE TAREAS")
    print("="*60)
    
    tareas_ejemplo = [
        "- [ ] Procesar ejemplos de Eduardo (hasta 30-Dic)",
        "- [ ] Implementar Dashboard (deadline: 2025-12-28)",
        "- [ ] Revisar contrato (para el 15/01/2026)",
        "- [ ] Tarea sin deadline",
    ]
    
    print("\nTareas priorizadas:")
    for tarea_info in prioritize_tasks(tareas_ejemplo):
        print(f"\n{tarea_info['urgency_text']}")
        print(f"  {tarea_info['task']}")
        print(f"  Score: {tarea_info['priority_score']}")
