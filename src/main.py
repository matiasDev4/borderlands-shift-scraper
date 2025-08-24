from utils.handler_inputs import check_input
from utils.browser import open_browser
from config.configuration import configuration
from colorama import init, Fore, Style

def start_menu():
    print(Fore.YELLOW + "[====] INICIANDO SCRIPT [====]")
    print(Fore.WHITE + "1 -> Ejecutar scraping")
    print(Fore.WHITE+ "2 -> Configuracion")
    
    option = check_input(Fore.BLUE + "SELECCIONAR OPCION: ")
    if option == 1:
        open_browser()
    if option == 2:
        configuration()


if __name__ == '__main__':
    start_menu()