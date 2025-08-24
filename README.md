## BORDERLANDS SHIFT SCRAPER
Este script en Python permite scrapear la web de Shift Codes para canjear automáticamente códigos y recibir recompensas en Borderlands.

### 🛠 Librerías utilizadas

[Playwright](https://playwright.dev/)
- Para interactuar con sitios web dinámicos (relleno de formularios, clicks, detección de cambios en el DOM).

[Colorama](https://recursospython.com/guias-y-manuales/colorama-texto-fondo-coloreados-la-consola/)
- Para mejorar la visualización en consola con logs a color.

Playwright siendo una libreria moderna, me permite interactuar con sitos webs dinamicos logrando relleno de formularios, clickear botones y detectar cambios en los elementos del DOM. <br/>
Colorama me permitio simplemente agregarle algo de colores a los logs en consola para hacerlo mas comodo visualmente

### ⚙️ Funcionamiento

Al ejecutar el script, se inicia un menú interactivo en consola con dos opciones: <br/>
Opción 1: Inicia el proceso de scraping y canje automático. <br/>
Opción 2: Permite configurar parámetros del navegador.

### 🔧 Configuración

Parámetros editables dentro del script:
- HEADLESS: Mostrar u ocultar el navegador durante la ejecución.
- VIEWPORT_WIDTH: Ancho del navegador (default: 1280px).
- VIEWPORT_HEIGHT: Alto del navegador (default: 720px).
- TIMEOUT: Tiempo de espera máximo para acciones con Playwright. <br />
Opciones avanzadas:
- USER_AGENT: Identificador del navegador (para evitar bloqueos en modo headless).
- CHROMIUM_ARG: Lista de argumentos adicionales para la instancia de Chromium.

### 🔑 Inicio de sesión

Es necesario contar con una cuenta SHIFT.
El script solicita credenciales y realiza automáticamente: <br/>
- Inicio de sesión. <br/>
- Detección de usuario. <br/>
- Navegación hasta la sección de recompensas. <br/>

Temporalmente se puede ingresar un código manualmente desde consola, en una actualización futura usaria una base de datos

### 🎮 Canje de códigos

- El script valida el código ingresado.
- Si es válido, lo aplica a todos los juegos disponibles.
- Si ya fue canjeado, muestra mensaje indicando el estado (ya utilizado o recompensa recibida).
- Si es inválido o expiró, muestra un error en consola.

Esto automatiza el proceso de:

- Pegar el código.
- Hacer clic en revisar.
- Canjear manualmente en cada juego válido.

### Imagenes de ejemplo:
- Menu interactivo + configuraciones <br/>
<img width="386" height="223" alt="menu" src="https://github.com/user-attachments/assets/0646558e-6fa4-4878-873e-08ea3b7a6c58" />

- Inicio del script + canjeo de juegos <br/>
<img width="347" height="271" alt="inicio" src="https://github.com/user-attachments/assets/8b0fae4a-c887-4abf-b092-a8824a377bef" />
