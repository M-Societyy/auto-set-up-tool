# Discord Server Setup Bot - M-Society

Este bot ha sido diseñado para facilitar la **creación y configuración rápida de servidores de Discord**, con plantillas automáticas, personalización de roles, canales de redes sociales y una experiencia completamente interactiva desde consola.

---

## 📦 Características Principales

✅ Configuración Turbo en 3 pasos  
✅ Configuración Avanzada Manual  
✅ Creación automática de categorías y canales  
✅ Generación de roles con colores y permisos  
✅ Creación de Webhooks para redes sociales (YouTube/Twitter)  
✅ Personalización total de estructura y permisos  
✅ Interfaz en consola con colores y estilo profesional  
✅ Comentarios útiles en el código para modificaciones futuras  

---

## ⚙️ Requisitos

### Python

- Python 3.8 o superior  
- Pip actualizado

### Librerías necesarias

Instálalas con:

```bash
pip install -r requirements.txt
````

O individualmente:

```bash
pip install discord.py colorama aiohttp
```

---



## 🚀 Cómo usarlo

### 1. Clona o descarga el repositorio

```bash
git clone https://github.com/usuario/DiscordSetupBot-MSociety.git
cd DiscordSetupBot-MSociety
```

### 2. Ejecuta el bot

```bash
python bot.py
```

### 3. Proporciona datos iniciales en consola:

* Token del bot
* ID del servidor (Server/Guild ID)

---

## 📋 Opciones del Menú Principal

Una vez el bot esté conectado, verás estas opciones en consola:

```txt
║ [1] Configuración Turbo (3 pasos)
║ [2] Configuración Avanzada Manual
║ [3] Configurar Webhooks (Redes Sociales)
║ [4] Personalización Avanzada de Roles
```

---

## 🔧 Descripción de Modos

### 🔹 \[1] Configuración Turbo

Solo responde 3 preguntas:

1. Tipo de servidor:

   * 1: Gaming
   * 2: Empresa
   * 3: Comunidad (por defecto usa gaming)

2. Nivel de seguridad (no implementado todavía, reservado para futuras actualizaciones)

3. Color principal (para aplicar tema visual en nombres):

   * rojo, azul, verde, morado

Esto genera canales, categorías y roles automáticamente según plantillas predefinidas.

---

### 🔹 \[2] Configuración Avanzada

Permite crear manualmente la estructura:

* Añade nombre de cada categoría
* Luego añade canales que contendrá
* Repite hasta dejar en blanco

Ideal para configuraciones 100% personalizadas.

---

### 🔹 \[3] Webhooks de Redes Sociales

Crea automáticamente una categoría `📡・REDES SOCIALES` y dentro:

* Canal `🐦・twitter` con webhook "Twitter Feed"
* Canal `📺・youtube` con webhook "YouTube Feed"

> Usa estas URLs de webhook en servicios como **IFTTT** o **Zapier** para automatización de publicaciones.

---

### 🔹 \[4] Personalización de Roles

Te permite crear roles personalizados ingresando:

* Nombre del rol
* Color (entre los disponibles en el script)
* Permisos (`admin`, `mod`, `basic`)

Los colores disponibles están en el diccionario `COLOR_MAP`, e incluyen:

* red, blue, green, morado, dark\_red, dark\_blue, dark\_grey

Los permisos disponibles están definidos en `PERM_PRESETS`.

---

## 💡 Consejos útiles

* Si el bot no responde, asegúrate de que el token esté correcto y que el bot esté **en el servidor** indicado.
* El bot **necesita permisos de administrador** en el servidor para poder borrar canales y crear nuevos.
* Si hay errores al crear canales o roles, puede deberse a limitaciones de Discord (por ejemplo, demasiadas solicitudes seguidas).
* Espera unos segundos entre cada acción si tienes muchos canales a crear.

---

## 🧑‍💻 Créditos

Proyecto desarrollado por **M-Society**
Inspirado en la necesidad de automatizar estructuras de servidores profesionales con calidad visual y rapidez.

---

## ⚠️ Aviso Legal

Este bot no realiza ninguna acción maliciosa.
Su propósito es **automatizar tareas de creación de servidores** para ahorrar tiempo y estandarizar la organización.
Eres completamente responsable del uso que le des.

---

## 🧪 Ejemplo visual de consola

[+] Conectado como SetupBot#1234

║ [1] Configuración Turbo (3 pasos)
║ [2] Configuración Avanzada Manual
║ [3] Configurar Webhooks (Redes Sociales)
║ [4] Personalización Avanzada de Roles

[?] Selecciona una opción
→ 1

[⚡] Modo Turbo Setup Activado
[i] Responde 3 preguntas clave para configuración automática

[?] Tipo de servidor [1] Gaming [2] Empresa [3] Comunidad
→ 1

[?] Nivel de seguridad [1] Básico [2] Medio [3] Alto
→ 2

[?] Color principal (rojo/azul/verde/morado)
→ morado

[+] Creando estructura turbo...
[+] Configurando roles automáticos...
[✓] Configuración turbo completada en 10 canales y 4 roles!



