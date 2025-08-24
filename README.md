## BORDERLANDS SHIFT SCRAPER
Este script en Python permite scrapear la web de Shift Codes para canjear automáticamente códigos y recibir recompensas en Borderlands.

### 🛠 Librerías utilizadas

[Playwright](https://playwright.dev/)
 → Para interactuar con sitios web dinámicos (relleno de formularios, clicks, detección de cambios en el DOM).

[Colorama](https://recursospython.com/guias-y-manuales/colorama-texto-fondo-coloreados-la-consola/)
 → Para mejorar la visualización en consola con logs a color.

Playwright siendo una libreria moderna, me permite interactuar con sitos webs dinamicos logrando relleno de formularios, clickear botones y detectar cambios en los elementos del DOM
Colorama me permitio simplemente agregarle algo de colores a los logs en consola para hacerlo mas comodo visualmente

### ⚙️ Funcionamiento

Al ejecutar el script, se inicia un menú interactivo en consola con dos opciones:
Opción 1: Inicia el proceso de scraping y canje automático.
Opción 2: Permite configurar parámetros del navegador.

### 🔧 Configuración

Parámetros editables dentro del script:
- HEADLESS: Mostrar u ocultar el navegador durante la ejecución.
- VIEWPORT_WIDTH: Ancho del navegador (default: 1280px).
- VIEWPORT_HEIGHT: Alto del navegador (default: 720px).
- TIMEOUT: Tiempo de espera máximo para acciones con Playwright.
Opciones avanzadas:
- USER_AGENT: Identificador del navegador (para evitar bloqueos en modo headless).
- CHROMIUM_ARG: Lista de argumentos adicionales para la instancia de Chromium.

### 🔑 Inicio de sesión

Es necesario contar con una cuenta SHIFT.
El script solicita credenciales y realiza automáticamente:
Inicio de sesión.
Detección de usuario.
Navegación hasta la sección de recompensas.

Se puede ingresar un código manualmente desde consola o, en un futuro, obtenerlos desde una base de datos.

### 🎮 Canje de códigos

- El script valida el código ingresado.
- Si es válido → lo aplica a todos los juegos disponibles.

- Si ya fue canjeado → muestra mensaje indicando el estado (ya utilizado o recompensa recibida).
- Si es inválido o expiró → muestra un error en consola.

Esto automatiza el proceso de:

- Pegar el código.
- Hacer clic en revisar.
- Canjear manualmente en cada juego válido.

### Imagenes de ejemplo:
<img width="219" height="79" alt="Captura de pantalla 2025-08-10 093837" src="https://github.com/user-attachments/assets/bf36707d-29f3-44d9-931c-1e5268b2f5b3" />
<img width="399" height="213" alt="Captura de pantalla 2025-08-10 093837" src="https://github.com/user-attachments/assets/5a897653-c251-4388-9cab-ec8c5d3f61d2" />
<img width="399" height="213" alt="Captura de pantalla 2025-08-10 093837" src="https://github.com/user-attachments/assets/cb5d471f-50f7-4cc7-886e-380af73b360a" />
<img width="399" height="213" alt="Captura de pantalla 2025-08-10 093837" src="https://github.com/user-attachments/assets/6e7aaac9-9522-4040-b62a-18fb61296bd3" />
