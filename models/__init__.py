#!/usr/bin/env python3
"""
Module for FileStorage (create a unique instance for my application)
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
