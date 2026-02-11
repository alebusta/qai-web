"""
QAI HQ Bot — State Service
Manejo de estado persistente (Firestore) para drafts y contexto.
"""
import os
import json
import logging
from datetime import datetime
from config import config

logger = logging.getLogger(__name__)

# Nombre de la colección en Firestore
COLLECTION_USERS = "users_bot_v2"

class StateService:
    """
    Servicio de persistencia.
    Usa Firestore si está disponible (GCP), o un archivo JSON local (Desarrollo).
    """

    def __init__(self):
        self.use_firestore = False
        self._db_client = None
        self._local_cache = {}
        self._local_file = "local_state.json"
        
        # Check environment to decide mode, but don't connect yet
        if os.getenv("GOOGLE_APPLICATION_CREDENTIALS") or os.getenv("K_SERVICE"):
            self.use_firestore = True
        else:
            self._load_local()

    @property
    def db(self):
        """Lazy init de Firestore client."""
        if self._db_client is None and self.use_firestore:
            try:
                from google.cloud import firestore
                self._db_client = firestore.Client()
                logger.info("🔥 Firestore conectado (lazy).")
            except Exception as e:
                logger.error(f"❌ Error conectando Firestore: {e}. Switch a local.")
                self.use_firestore = False
                self._load_local()
        return self._db_client

    def _load_local(self):
        """Carga estado desde archivo local."""
        if os.path.exists(self._local_file):
            try:
                with open(self._local_file, "r", encoding="utf-8") as f:
                    self._local_cache = json.load(f)
            except Exception:
                self._local_cache = {}

    def _save_local(self):
        """Guarda estado en archivo local."""
        with open(self._local_file, "w", encoding="utf-8") as f:
            json.dump(self._local_cache, f, indent=2, ensure_ascii=False)

    def set_user_state(self, chat_id: int, key: str, value: any):
        """Guarda un valor en el estado del usuario."""
        chat_str = str(chat_id)
        if self.use_firestore:
            try:
                doc_ref = self.db.collection(COLLECTION_USERS).document(chat_str)
                doc_ref.set({key: value}, merge=True)
            except Exception as e:
                logger.error(f"❌ Error escribiendo en Firestore: {e}")
        else:
            if chat_str not in self._local_cache:
                self._local_cache[chat_str] = {}
            self._local_cache[chat_str][key] = value
            self._save_local()

    def get_user_state(self, chat_id: int, key: str) -> any:
        """Obtiene un valor del estado del usuario."""
        chat_str = str(chat_id)
        if self.use_firestore:
            try:
                doc_ref = self.db.collection(COLLECTION_USERS).document(chat_str)
                doc = doc_ref.get()
                if doc.exists:
                    return doc.to_dict().get(key)
                return None
            except Exception as e:
                logger.error(f"❌ Error leyendo de Firestore: {e}")
                return None
        else:
            return self._local_cache.get(chat_str, {}).get(key)
    
    def save_draft(self, chat_id: int, draft_data: dict):
        """Guarda un borrador de email."""
        self.set_user_state(chat_id, "current_draft", draft_data)
        
    def get_draft(self, chat_id: int) -> dict:
        """Recupera el borrador actual."""
        return self.get_user_state(chat_id, "current_draft")

    def clear_draft(self, chat_id: int):
        """Borra el borrador actual."""
        self.set_user_state(chat_id, "current_draft", None)

# Singleton
_state_instance = None

def get_state() -> StateService:
    global _state_instance
    if _state_instance is None:
        _state_instance = StateService()
    return _state_instance
