#!/usr/bin/env python3
"""
Audit Consistency - QAI Memory Institutional Integrity Checker

Este script verifica la consistencia de la memoria institucional de QAI:
- Estructura de agentes completa
- Referencias cruzadas válidas
- Sincronización de fechas
- Playbooks documentados

Uso:
    python audit_consistency.py
    python audit_consistency.py --verbose
"""

import os
import re
from pathlib import Path
from datetime import datetime
from typing import List, Tuple, Dict

# Colores para terminal
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def print_success(msg: str):
    print(f"{Colors.GREEN}✅ {msg}{Colors.RESET}")

def print_warning(msg: str):
    print(f"{Colors.YELLOW}⚠️  {msg}{Colors.RESET}")

def print_error(msg: str):
    print(f"{Colors.RED}❌ {msg}{Colors.RESET}")

def print_info(msg: str):
    print(f"{Colors.BLUE}ℹ️  {msg}{Colors.RESET}")

def print_header(msg: str):
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}{msg}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.RESET}\n")

# Rutas base
BASE_DIR = Path(__file__).parent.parent.parent
QAICORE_DIR = BASE_DIR / "QaiCore"
TORRE_DIR = BASE_DIR / "TorreDeControl"
AGENTS_DIR = QAICORE_DIR / "agents"
PLAYBOOKS_DIR = QAICORE_DIR / "playbooks"

def check_agent_structure() -> Tuple[int, int]:
    """Verifica que todos los agentes tengan estructura completa."""
    print_header("1. Verificando Estructura de Agentes")
    
    required_files = ["profile.md", "system_prompt.md", "tools.json"]
    agents = ["finn", "lex", "nzero"]
    
    passed = 0
    failed = 0
    
    for agent in agents:
        agent_dir = AGENTS_DIR / agent
        print(f"\n{Colors.BOLD}Agente: {agent.upper()}{Colors.RESET}")
        
        if not agent_dir.exists():
            print_error(f"Directorio no existe: {agent_dir}")
            failed += 1
            continue
        
        agent_passed = True
        for required_file in required_files:
            file_path = agent_dir / required_file
            if file_path.exists():
                print_success(f"{required_file} existe")
            else:
                print_error(f"{required_file} NO EXISTE")
                agent_passed = False
        
        # Verificar knowledge_base
        kb_dir = agent_dir / "knowledge_base"
        if kb_dir.exists():
            kb_files = list(kb_dir.rglob("*.md"))
            print_success(f"knowledge_base/ existe ({len(kb_files)} archivos)")
        else:
            print_error("knowledge_base/ NO EXISTE")
            agent_passed = False
        
        if agent_passed:
            passed += 1
        else:
            failed += 1
    
    return passed, failed

def check_playbooks_documentation() -> Tuple[int, int]:
    """Verifica que todos los playbooks estén documentados en README."""
    print_header("2. Verificando Documentación de Playbooks")
    
    # Listar playbooks reales
    playbook_files = [f.name for f in PLAYBOOKS_DIR.glob("*.md") if f.name != "README.md"]
    
    # Leer README
    readme_path = PLAYBOOKS_DIR / "README.md"
    if not readme_path.exists():
        print_error("playbooks/README.md NO EXISTE")
        return 0, len(playbook_files)
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        readme_content = f.read()
    
    passed = 0
    failed = 0
    
    print(f"\n{Colors.BOLD}Playbooks encontrados: {len(playbook_files)}{Colors.RESET}\n")
    
    for playbook in sorted(playbook_files):
        if playbook in readme_content:
            print_success(f"{playbook} documentado")
            passed += 1
        else:
            print_error(f"{playbook} NO DOCUMENTADO en README")
            failed += 1
    
    return passed, failed

def check_torre_sync() -> Tuple[int, int]:
    """Verifica sincronización de fechas en TorreDeControl."""
    print_header("3. Verificando Sincronización de Fechas (TorreDeControl)")
    
    files_to_check = {
        "STATUS.md": TORRE_DIR / "STATUS.md",
        "INBOX.md": TORRE_DIR / "INBOX.md",
        "AGENT_ACTIVITY.md": TORRE_DIR / "AGENT_ACTIVITY.md"
    }
    
    dates = {}
    passed = 0
    failed = 0
    
    # Extraer fechas
    for name, path in files_to_check.items():
        if not path.exists():
            print_error(f"{name} NO EXISTE")
            failed += 1
            continue
        
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Buscar patrón de fecha
        patterns = [
            r'Última actualización[:\s]+(\d{1,2})\s+de\s+(\w+)\s+(\d{4})',
            r'Última actualización[:\s]+(\d{1,2})-(\w+)-(\d{4})',
        ]
        
        date_found = None
        for pattern in patterns:
            match = re.search(pattern, content, re.IGNORECASE)
            if match:
                date_found = f"{match.group(1)}-{match.group(2)}-{match.group(3)}"
                break
        
        if date_found:
            dates[name] = date_found
            print_info(f"{name}: {date_found}")
        else:
            print_warning(f"{name}: Fecha no encontrada")
            dates[name] = "N/A"
    
    # Verificar consistencia
    unique_dates = set(d for d in dates.values() if d != "N/A")
    
    if len(unique_dates) <= 2:  # Permitir hasta 2 fechas diferentes (razonable)
        print_success(f"Fechas consistentes (máximo 2 diferentes)")
        passed += 1
    else:
        print_warning(f"Fechas desincronizadas ({len(unique_dates)} fechas diferentes)")
        failed += 1
    
    return passed, failed

def check_broken_links() -> Tuple[int, int]:
    """Verifica que los links internos no estén rotos."""
    print_header("4. Verificando Referencias Cruzadas (Links)")
    
    # Archivos a verificar
    files_to_scan = [
        QAICORE_DIR / "README.md",
        TORRE_DIR / "README.md",
        QAICORE_DIR / "agents" / "KNOWLEDGE_BASE_INDEX.md"
    ]
    
    passed = 0
    failed = 0
    
    for file_path in files_to_scan:
        if not file_path.exists():
            print_warning(f"Archivo no existe: {file_path.name}")
            continue
        
        print(f"\n{Colors.BOLD}Verificando: {file_path.name}{Colors.RESET}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Buscar links file:///
        file_links = re.findall(r'file:///([^\)]+)', content)
        
        if not file_links:
            print_info("No se encontraron links file:///")
            continue
        
        for link in file_links:
            # Convertir a Path
            # Normalizar: file:///c:/Users/... → c:/Users/...
            link_clean = link.replace('file:///', '').replace('/', '\\')
            link_path = Path(link_clean)
            
            if link_path.exists():
                passed += 1
            else:
                print_error(f"Link roto: {link[:80]}...")
                failed += 1
    
    if failed == 0:
        print_success(f"Todos los links válidos ({passed} verificados)")
    
    return passed, failed

def check_required_files() -> Tuple[int, int]:
    """Verifica que archivos críticos existan."""
    print_header("5. Verificando Archivos Críticos")
    
    required_files = [
        (QAICORE_DIR / "README.md", "QaiCore/README.md"),
        (QAICORE_DIR / "requirements.txt", "QaiCore/requirements.txt"),
        (QAICORE_DIR / "qrun.bat", "QaiCore/qrun.bat"),
        (TORRE_DIR / "README.md", "TorreDeControl/README.md"),
        (TORRE_DIR / "STATUS.md", "TorreDeControl/STATUS.md"),
        (TORRE_DIR / "INBOX.md", "TorreDeControl/INBOX.md"),
        (TORRE_DIR / "CHANGELOG.md", "TorreDeControl/CHANGELOG.md"),
        (TORRE_DIR / "AGENT_ACTIVITY.md", "TorreDeControl/AGENT_ACTIVITY.md"),
        (PLAYBOOKS_DIR / "README.md", "playbooks/README.md"),
    ]
    
    passed = 0
    failed = 0
    
    for file_path, display_name in required_files:
        if file_path.exists():
            print_success(f"{display_name} existe")
            passed += 1
        else:
            print_error(f"{display_name} NO EXISTE")
            failed += 1
    
    return passed, failed

def main():
    """Ejecuta todos los tests de consistencia."""
    print(f"\n{Colors.BOLD}{Colors.BLUE}")
    print("╔════════════════════════════════════════════════════════════╗")
    print("║   QAI - Audit de Consistencia de Memoria Institucional    ║")
    print("╚════════════════════════════════════════════════════════════╝")
    print(f"{Colors.RESET}\n")
    
    total_passed = 0
    total_failed = 0
    
    # Test 1: Estructura de agentes
    passed, failed = check_agent_structure()
    total_passed += passed
    total_failed += failed
    
    # Test 2: Playbooks documentados
    passed, failed = check_playbooks_documentation()
    total_passed += passed
    total_failed += failed
    
    # Test 3: Sincronización de fechas
    passed, failed = check_torre_sync()
    total_passed += passed
    total_failed += failed
    
    # Test 4: Links rotos
    passed, failed = check_broken_links()
    total_passed += passed
    total_failed += failed
    
    # Test 5: Archivos críticos
    passed, failed = check_required_files()
    total_passed += passed
    total_failed += failed
    
    # Resumen final
    print_header("RESUMEN FINAL")
    
    total_tests = total_passed + total_failed
    success_rate = (total_passed / total_tests * 100) if total_tests > 0 else 0
    
    print(f"{Colors.BOLD}Total de verificaciones: {total_tests}{Colors.RESET}")
    print_success(f"Pasadas: {total_passed}")
    if total_failed > 0:
        print_error(f"Fallidas: {total_failed}")
    else:
        print_success(f"Fallidas: {total_failed}")
    
    print(f"\n{Colors.BOLD}Tasa de éxito: {success_rate:.1f}%{Colors.RESET}\n")
    
    if total_failed == 0:
        print(f"{Colors.GREEN}{Colors.BOLD}🎉 ¡PERFECTO! Memoria institucional 100% consistente{Colors.RESET}\n")
        return 0
    elif success_rate >= 90:
        print(f"{Colors.YELLOW}{Colors.BOLD}⚠️  Memoria institucional en buen estado, pero con algunos puntos de mejora{Colors.RESET}\n")
        return 1
    else:
        print(f"{Colors.RED}{Colors.BOLD}❌ Se detectaron problemas de consistencia que requieren atención{Colors.RESET}\n")
        return 2

if __name__ == "__main__":
    import sys
    sys.exit(main())
