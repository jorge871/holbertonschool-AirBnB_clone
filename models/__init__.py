#!/usr/bin/python3
"""init file for storage"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
