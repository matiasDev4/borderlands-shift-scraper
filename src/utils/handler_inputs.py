from config.script_config import COLORS
import re 

def check_input(message: str) -> int:
    while True:
        try:
            value = int(input(message).strip())
            if value in (1,2):
                return value
            else:
                print(COLORS['error'] + "[ERROR]: " + COLORS['text'] + "Solo se acepta 1 o 2")
        except ValueError:
            print(COLORS['error'] + "[ERROR]: " + COLORS['text'] + "Debe ingresar un numero")

def check_input_str(message: str) -> bool:
    while True:
        option = input(message).strip().upper()
        if option in ('S', 'N'):
            return option == "S"
        print(COLORS['error'] + "[ERROR]: " + COLORS['text'] + "Respuesta invalida")
        
def check_input_int(message: str, default: int = None) -> int:
    while True:
        option = int(input(f"{message} " + (f"[default: {default}]" if default else "") + ": ").strip())
        if option:
            return option
        if default is not None:
            return default
        print(COLORS['error'] + "[ERROR]: " + COLORS['text'] + "No se puede dejar vacio")

def check_input_ms(message: str, default: int = None, min_value: int = None) -> int:
    while True:
        option = input(f"{message} " + (f"[default: {default}]" if default else "") + ": ").strip()
        if option == '' and default is not None:
            return default
        if option.isdigit():
            number = int(option)
            if min_value is None or number >= min_value:
                return number
            print(COLORS['error'] + "[ERROR]: " + COLORS['text'] + f"Debe ser mayor o igual al minimo {min_value}")
        print(COLORS['error'] + "[ERROR]: " + COLORS['text'] + "Numero invalido")

def check_code(message: str) -> str:
    while True:
        value = input(message).strip().upper()
        if len(value) != 29:
            print(COLORS['error'] + "[ERROR]" + COLORS['text'] +": El codigo no es valido")
            continue
        if not re.match(r'^[A-Z0-9-]+$', value):
            print(COLORS['error'] + "[ERROR]" + COLORS['text'] +": Verifique la cadena de texto")
            continue
   
        return value
