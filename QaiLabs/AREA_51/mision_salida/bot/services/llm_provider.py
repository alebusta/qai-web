"""
QAI HQ Bot — LLM Provider (Agnostic)
Capa de abstracción para múltiples LLMs: Gemini, Groq, Claude.
"""
import logging
from abc import ABC, abstractmethod
from config import config

logger = logging.getLogger(__name__)


class LLMProvider(ABC):
    """Interface base para proveedores de LLM."""

    @abstractmethod
    def chat(self, prompt: str, system_instruction: str = "") -> str:
        """Envía un prompt al LLM y retorna la respuesta."""
        ...

    @property
    @abstractmethod
    def name(self) -> str:
        """Nombre del proveedor."""
        ...


class GeminiProvider(LLMProvider):
    """Proveedor de Google Gemini."""

    def __init__(self):
        import google.generativeai as genai

        genai.configure(api_key=config.GEMINI_API_KEY)
        self._model = genai.GenerativeModel("gemini-2.0-flash")
        logger.info("🤖 Gemini Provider inicializado (gemini-2.0-flash)")

    @property
    def name(self) -> str:
        return "Gemini"

    def chat(self, prompt: str, system_instruction: str = "") -> str:
        try:
            full_prompt = f"{system_instruction}\n\n{prompt}" if system_instruction else prompt
            response = self._model.generate_content(full_prompt)
            return response.text
        except Exception as e:
            logger.error("❌ Error Gemini: %s", e)
            return f"⚠️ Error al consultar Gemini: {str(e)}"


class GroqProvider(LLMProvider):
    """Proveedor de Groq (modelos open source como Llama, Mixtral)."""

    def __init__(self):
        self._api_key = config.GROQ_API_KEY
        self._model = "llama-3.3-70b-versatile"
        logger.info("🤖 Groq Provider inicializado (%s)", self._model)

    @property
    def name(self) -> str:
        return "Groq"

    def chat(self, prompt: str, system_instruction: str = "") -> str:
        import requests

        try:
            messages = []
            if system_instruction:
                messages.append({"role": "system", "content": system_instruction})
            messages.append({"role": "user", "content": prompt})

            response = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {self._api_key}",
                    "Content-Type": "application/json",
                },
                json={"model": self._model, "messages": messages},
                timeout=30,
            )
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]
        except Exception as e:
            logger.error("❌ Error Groq: %s", e)
            return f"⚠️ Error al consultar Groq: {str(e)}"


class ClaudeProvider(LLMProvider):
    """Proveedor de Anthropic Claude (stub para futuro)."""

    def __init__(self):
        logger.info("🤖 Claude Provider inicializado (stub)")

    @property
    def name(self) -> str:
        return "Claude"

    def chat(self, prompt: str, system_instruction: str = "") -> str:
        return "⚠️ Claude Provider aún no implementado. Usa Gemini o Groq."


# === Factory ===

_PROVIDERS = {
    "gemini": GeminiProvider,
    "groq": GroqProvider,
    "claude": ClaudeProvider,
}


def get_llm(provider_name: str | None = None) -> LLMProvider:
    """
    Factory para obtener un proveedor de LLM.
    
    Args:
        provider_name: 'gemini', 'groq', o 'claude'. Si None, usa config.
    """
    name = (provider_name or config.LLM_PROVIDER).lower()

    if name not in _PROVIDERS:
        logger.warning("Proveedor '%s' no reconocido, usando Gemini", name)
        name = "gemini"

    return _PROVIDERS[name]()
