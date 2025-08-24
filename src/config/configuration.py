from utils.handler_inputs import check_input_str, check_input_int, check_input_ms
from config.script_config import CONFIG, COLORS
from utils.browser import open_browser

def configuration():
    CONFIG['headless'] = check_input_str(COLORS['text'] + '-> MODO HEADLESS [S/N]: ')
    CONFIG['viewport_width'] = check_input_int(COLORS['text'] + "-> ANCHO DE PANTALLA: ", default=1280)
    CONFIG['viewport_height'] = check_input_int(COLORS['text'] + "-> ALTO DE PANTALLA: ", default=720)
    CONFIG['timeout'] = check_input_ms(COLORS['text'] + "-> TIEMPO DE ESPERA [milisegundos]: ", default=5000, min_value=2000)

    print(COLORS['message'] + "\n===============[CONFIGURACIONES]==================")
    print(COLORS['text'] + f"-> MODO HEADLESS: {'SI' if CONFIG['headless'] else 'NO'}")
    print(COLORS['text'] + f"-> TAMAÑO DE PANTALLA: {CONFIG['viewport_width']} X {CONFIG['viewport_height']}")
    print(COLORS['text'] + f"-> TIEMPO DE ESPERA: {CONFIG['timeout']} ms")
    print(COLORS['message'] + "==================================================\n")
    
    if check_input_str(COLORS['text'] + "-> INICIAR SCRAPING [S/N]: "):
        open_browser()