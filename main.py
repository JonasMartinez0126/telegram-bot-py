
import telebot
from config import TELEGRAM_TOKEN
from datetime import datetime

# Importar las funciones de persistencia
from agendaPersistencia import cargar_agenda, guardar_agenda

# Token del bot
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Estructura de datos para almacenar la agenda en memoria
agenda = cargar_agenda()

# Se activa con /start y da la bienvenida mostrando las instrucciones para los comandos
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, (
        "¡Bienvenido al Bot de Agenda de Clases! Usa:\n"
        "/agendar <fecha> <hora> <nombre> - para agregar una clase\n"
        "/veragenda - para ver la agenda\n"
        "/eliminar <número> - para eliminar una clase específica"
    ))

# Permite agendar una clase. El usuario debe seguir el formato /agendar DD-MM-YYYY HH:MM NombreClase
@bot.message_handler(commands=['agendar'])
def agendar(message):
    try:
        # Verifica si el usuario proporcionó suficientes argumentos
        if len(message.text.split()) < 4:
            raise IndexError("No se proporcionaron suficientes argumentos.")
        
        # Dividir el mensaje en partes
        _, date_str, time_str, *class_name = message.text.split()
        class_name = ' '.join(class_name)
        
        # Validar formato de fecha y hora
        try:
            date_time = datetime.strptime(f"{date_str} {time_str}", "%d-%m-%Y %H:%M")
        except ValueError:
            raise ValueError("Formato de fecha y hora incorrecto. Usa DD-MM-YYYY HH:MM.")
        
        # Guardar en la agenda y persistir en el archivo
        agenda.append({"date_time": date_time.strftime("%d-%m-%Y %H:%M"), "class_name": class_name})
        guardar_agenda(agenda)
        bot.reply_to(message, f"Clase '{class_name}' agendada para {date_time}.")
    
    except IndexError:
        bot.reply_to(message, "Formato incorrecto. Usa: /agendar DD-MM-YYYY HH:MM NombreClase")
    except ValueError as e:
        bot.reply_to(message, str(e))

# Muestra las clases guardadas en la agenda
@bot.message_handler(commands=['veragenda'])
def veragenda(message):
    try:
        if agenda:
            message_text = "Tu agenda de clases:\n"
            for i, event in enumerate(agenda, start=1):
                message_text += f"{i}. {event['class_name']} - {event['date_time']}\n"
        else:
            message_text = "No tienes clases agendadas."
        bot.reply_to(message, message_text)
    except Exception as e:
        bot.reply_to(message, f"Error al mostrar la agenda: {e}")

    
# Elimina una clase usando su número de posición en la lista de clases agendadas
@bot.message_handler(commands=['eliminar'])
def eliminar(message):
    try:
        # Verificar que se proporcionó un índice
        if len(message.text.split()) < 2:
            raise IndexError("No se proporcionó el índice de la clase a eliminar.")
        
        # Obtener el índice de la clase en la agenda
        index = int(message.text.split()[1]) - 1
        
        # Validar que el índice esté en el rango de la agenda
        if 0 <= index < len(agenda):
            removed_event = agenda.pop(index)
            guardar_agenda(agenda)  # Guardar la agenda actualizada en el archivo
            bot.reply_to(message, f"Clase '{removed_event['class_name']}' eliminada de la agenda.")
        else:
            bot.reply_to(message, "Número de clase no válido. Usa /veragenda para ver los números válidos.")
    
    except IndexError:
        bot.reply_to(message, "Formato incorrecto. Usa: /eliminar <númeroClase>")
    except ValueError:
        bot.reply_to(message, "El índice debe ser un número entero. Usa: /eliminar <númeroClase>")
    except Exception as e:
        bot.reply_to(message, f"Error al eliminar la clase: {e}")


# Ejecutar el bot
bot.polling()
