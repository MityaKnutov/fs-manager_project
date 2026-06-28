import os
import shutil
import logging

def list_directory(path):
    try:
        return os.listdir(path)
    except Exception as e:
        logging.error(f"Error listing directory {path}: {e}")
        return []

def create_folder(path):
    try:
        os.makedirs(path, exist_ok=True)
        return True
    except Exception as e:
        logging.error(f"Error creating folder {path}: {e}")
        return False

def delete(path):
    try:
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
        return True
    except Exception as e:
        logging.error(f"Ошибка удаления {path}: {e}")
        return False

def move(source, destination):
    try:
        shutil.move(source, destination)
        return True
    except Exception as e:
        logging.error(f"Ошибка перемещения {source} в {destination}: {e}")
        return False

def copy(source, destination):
    try:
        if os.path.isdir(source):
            shutil.copytree(source, destination)
        else:
            shutil.copy2(source, destination)
        return True
    except Exception as e:
        logging.error(f"Ошибка копирования {source} в {destination}: {e}")
        return False