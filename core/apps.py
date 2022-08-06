"""Configurações paras apps do App core"""
from django.apps import AppConfig


class CoreConfig(AppConfig):
    """Configurações do core"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "core"
