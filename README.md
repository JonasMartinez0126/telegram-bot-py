# Bot de Agenda de Clases en Telegram

Este es un bot de Telegram que permite gestionar una agenda de clases. Puedes agregar, ver y eliminar clases de tu agenda mediante comandos sencillos.

## Requisitos Previos

Asegúrate de tener instalado Python 3.x y `pip` en tu sistema. También necesitarás crear un bot en Telegram usando [@BotFather](https://t.me/botfather) para obtener tu token.

## Configuración

### 1. Agregar el archivo de configuración

Crea un archivo llamado `config.py` en el directorio raíz del proyecto y añade la siguiente línea:

```python
TELEGRAM_TOKEN = ""
```

Coloca el token de tu bot de Telegram entre las comillas.

### 2. Crear un entorno virtual

Abre Visual Studio Code o tu IDE de preferencia y genera un entorno virtual. Ejecuta el siguiente comando en la terminal:

```bash
python -m venv env
```

### 3. Activar el entorno virtual

Luego, activa el entorno virtual ejecutando:

- En Windows:

```bash
.\env\Scripts\activate
```

Si encuentras un error, ejecuta el siguiente comando antes de intentar activar el entorno nuevamente:

```bash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

- En macOS/Linux:

```bash
source env/bin/activate
```

### 4. Instalar dependencias

Ejecuta el siguiente comando para instalar todos los paquetes requeridos:

```bash
pip install -r requirements.txt
```

### 5. Ejecutar el bot

Finalmente, ejecuta el bot con el siguiente comando:

```bash
python main.py
```

### 6. Interactuar con el bot

Abre Telegram, busca `@BotFather`, y envía el comando `/start` para comenzar a interactuar con tu bot.

## Comandos Disponibles

- `/start`: Muestra un mensaje de bienvenida y las instrucciones para usar el bot.
- `/agendar <fecha> <hora> <nombre>`: Agrega una clase a tu agenda.
- `/veragenda`: Muestra todas las clases agendadas.
- `/eliminar <número>`: Elimina una clase específica de la agenda.