import json
import os

# Archivo para guardar la agenda
AGENDA_FILE = "agenda.json"

# Lee el archivo JSON y devuelve la agenda si existe; si no, devuelve una lista vacia. Guardamos la fecha y hora en formato de cadena (%d-%m-%Y %H:%M) para evitar problemas de serialización
def cargar_agenda():
    if os.path.exists(AGENDA_FILE):
        with open(AGENDA_FILE, "r") as f:
            return json.load(f)
    return []

# Guarda la agenda actual en el archivo JSON usando json.dump y convierte la fecha en una cadena para almacenarla correctamente
def guardar_agenda(agenda):
    with open(AGENDA_FILE, "w") as f:
        json.dump(agenda, f, default=str, indent=4)