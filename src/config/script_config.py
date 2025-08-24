import os
from dotenv import load_dotenv
from colorama import Fore
load_dotenv('.env')


CONFIG = {
    'headless': True,
    'chromium_arg':['--no-sandbox', '--disable-setuid-sandbox'],
    'viewport_width': 1280,
    'viewport_height': 720,
    'timeout': 5000,
    'user_agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'email':os.getenv('EMAIL'),
    'password':os.getenv('PASSWORD'),
    'login_url':os.getenv('LOGIN_URL'),
    'account_url':os.getenv('ACCOUNT_URL'),
    'codes_url':os.getenv('SEND_CODES_URL'),
    'rewards_url':os.getenv('REWARDS_URL')
}


COLORS = {
    'succes': Fore.GREEN,
    'error': Fore.RED,
    'alert': Fore.YELLOW,
    'text': Fore.WHITE,
    'message': Fore.CYAN
}

    