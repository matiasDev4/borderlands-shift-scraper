from playwright.sync_api import sync_playwright
from config.script_config import CONFIG, COLORS
from utils.handler_inputs import check_code

def open_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=CONFIG['headless'], args=CONFIG['chromium_arg'])
        context = browser.new_context(viewport={"width":CONFIG['viewport_width'], "height":CONFIG['viewport_height']},user_agent=CONFIG['user_agent'])
        page = context.new_page()
        login_shift(page)
        account_data(page)
        rewards(page)
        

def login_shift(page):
    print(COLORS['text'] + '-> INICIANDO SESION')
    page.goto('https://shift.gearboxsoftware.com/home')
    page.locator('input[name="user[email]"]').fill(CONFIG['email'])
    page.locator('input[name="user[password]"]').fill(CONFIG['password'])
    page.click('input[type="submit"]')
    
def account_data(page):
    print(COLORS['text'] + '-> INGRESANDO A /account')
    page.goto(CONFIG['account_url'])
    username = page.locator('id=current_display_name').text_content()
    print(COLORS['text'] + f"-> USERNAME ACCOUNT: {username}")

def rewards(page):
    print(COLORS['text'] + "-> INGRESANDO A /rewards")
    page.goto(CONFIG['rewards_url'])
    code = check_code(COLORS['message'] + '[INGRESAR CODIGO]: ')
    print(COLORS['text'] + "-> PROBANDO CODIGO SHIFT")

    redeem_code(page, code)


def redeem_code(page, code):
    redeemed_titles = set()
    while True:

        page.goto(CONFIG['rewards_url'])
        page.query_selector('#shift_code_input').fill(code)
        page.click('button[id="shift_code_check"]')


        container = page.wait_for_selector('.sh_status_container_code_redemption', state='attached', timeout=5000)
        page.wait_for_function("container => window.getComputedStyle(container).display !== 'none'", arg=container)


        page.wait_for_selector("#code_results h2", state="attached", timeout=5000)
        titles = page.locator("#code_results h2").all_text_contents()
        buttons = page.locator("input[name='commit']")


        new_buttons = [(title, buttons.nth(i)) for i, title in enumerate(titles) if title not in redeemed_titles]

        if not new_buttons:
            print(COLORS['succes'] + "[SUCCESS]: " + COLORS['text'] + "Todos los codigos fueron canjeados")
            break


        title, button = new_buttons[0]
        print(COLORS['message'] + f"[CANJEANDO]: {title}")
        button.click()
        page.wait_for_selector('.sh_status_container_code_redemption', state='attached', timeout=5000)
        message = page.wait_for_selector('div.alert.notice', state='attached', timeout=5000)
        if message.is_visible():
            print(COLORS['alert'] + '[ALERT]: ' + COLORS['text'] + "Este codigo ya fue canjeado")
        page.wait_for_timeout(2000)
        redeemed_titles.add(title)
    
    
        
        
    
    
    
    


    
