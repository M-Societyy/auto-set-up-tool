# Discord Server Setup Bot - M-Society
# Antes de q digas q es IA por los comentarios en el script, lo comentamos por si alguien quiere hacer modificaciones.


import discord
from discord.ext import commands
import asyncio
from colorama import Fore, init, Style
import os
import json
import aiohttp

# Inicializar colorama
init()
os.system("title Discord Server Setup Bot - M-Society")
os.system("cls" if os.name == "nt" else "clear")

# Banner
banner = """
                         ███▄ ▄███▓  ██████  ▒█████   ▄████▄   ██▓▓█████▄▄▄█████▓▓██   ██▓
                        ▓██▒▀█▀ ██▒▒██    ▒ ▒██▒  ██▒▒██▀ ▀█  ▓██▒▓█   ▀▓  ██▒ ▓▒ ▒██  ██▒
                        ▓██    ▓██░░ ▓██▄   ▒██░  ██▒▒▓█    ▄ ▒██▒▒███  ▒ ▓██░ ▒░  ▒██ ██░
                        ▒██    ▒██   ▒   ██▒▒██   ██░▒▓▓▄ ▄██▒░██░▒▓█  ▄░ ▓██▓ ░   ░ ▐██▓░
                        ▒██▒   ░██▒▒██████▒▒░ ████▓▒░▒ ▓███▀ ░░██░░▒████▒ ▒██▒ ░   ░ ██▒▓░
                        ░ ▒░   ░  ░▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░ ░▒ ▒  ░░▓  ░░ ▒░ ░ ▒ ░░      ██▒▒▒ 
                        ░  ░      ░░ ░▒  ░ ░  ░ ▒ ▒░   ░  ▒    ▒ ░ ░ ░  ░   ░     ▓██ ░▒░ 
                        ░      ░   ░  ░  ░  ░ ░ ░ ▒  ░         ▒ ░   ░    ░       ▒ ▒ ░░  
                        ░         ░      ░ ░  ░ ░       ░     ░  ░         ░ ░      
                                              ░                            ░ ░     
"""

def show_gradient_banner():
    start_color = (255, 0, 0)    
    end_color = (128, 0, 255)    
    
    def generate_gradient(start, end, steps):
        gradient = []
        for i in range(steps):
            r = int(start[0] + (end[0] - start[0]) * i / steps)
            g = int(start[1] + (end[1] - start[1]) * i / steps)
            b = int(start[2] + (end[2] - start[2]) * i / steps)
            gradient.append((r, g, b))
        return gradient
    
    gradient = generate_gradient(start_color, end_color, len(banner))
    for i, char in enumerate(banner):
        r, g, b = gradient[i]
        print(f"\033[38;2;{r};{g};{b}m{char}", end="")
    print("\033[0m")

show_gradient_banner()


# Configuración inicial
def get_input(prompt):
    print(f"{Fore.WHITE}[{Fore.CYAN}?{Fore.WHITE}] {prompt}")
    return input(f"{Fore.WHITE}→ {Fore.CYAN}")

# Configuración Turbo
async def turbo_setup():
    print(f"\n{Fore.WHITE}[{Fore.MAGENTA}⚡{Fore.WHITE}] {Fore.YELLOW}Modo Turbo Setup Activado{Style.RESET_ALL}")
    print(f"{Fore.WHITE}[{Fore.CYAN}i{Fore.WHITE}] Responde 3 preguntas clave para configuración automática\n")
    
    server_type = get_input(f"Tipo de servidor {Fore.WHITE}[{Fore.CYAN}1{Fore.WHITE}] Gaming {Fore.WHITE}[{Fore.CYAN}2{Fore.WHITE}] Empresa {Fore.WHITE}[{Fore.CYAN}3{Fore.WHITE}] Comunidad")
    security_level = get_input(f"Nivel de seguridad {Fore.WHITE}[{Fore.CYAN}1{Fore.WHITE}] Básico {Fore.WHITE}[{Fore.CYAN}2{Fore.WHITE}] Medio {Fore.WHITE}[{Fore.CYAN}3{Fore.WHITE}] Alto")
    main_color = get_input(f"Color principal {Fore.WHITE}({Fore.RED}rojo{Fore.WHITE}/{Fore.BLUE}azul{Fore.WHITE}/{Fore.GREEN}verde{Fore.WHITE}/{Fore.MAGENTA}morado{Fore.WHITE})")
    
    return {
        "server_type": server_type,
        "security_level": security_level,
        "main_color": main_color.lower()
    }

# Plantillas de configuración
TEMPLATES = {
    "gaming": {
        "estructura": {
            "🎮・GAMING": ["📢・anuncios", "💬・general", "🎮・juegos", "📸・clips"],
            "📢・COMUNIDAD": ["💬・charla", "🎭・memes", "🎨・creaciones"],
            "🔊・VOZ": ["🎤・general", "🎶・karaoke", "🎮・juegos"]
        },
        "roles": {
            "👑・Dueño": {"color": "red", "perms": "admin"},
            "⚡・Moderador": {"color": "blue", "perms": "mod"},
            "🎮・Gamer": {"color": "green", "perms": "basic"}
        }
    },
    "empresa": {
        "estructura": {
            "📌・INFORMACIÓN": ["📢・anuncios", "📅・eventos", "🏢・normativas"],
            "💼・DEPARTAMENTOS": ["📊・ventas", "🖥️・TI", "📦・logística"],
            "🤝・COMUNICACIÓN": ["💬・general", "📩・sugerencias"]
        },
        "roles": {
            "👔・Director": {"color": "dark_red", "perms": "admin"},
            "🖋️・Gerente": {"color": "dark_blue", "perms": "mod"},
            "👨‍💼・Empleado": {"color": "dark_grey", "perms": "basic"}
        }
    }
}

COLOR_MAP = {
    "red": discord.Colour.red(),
    "blue": discord.Colour.blue(),
    "green": discord.Colour.green(),
    "morado": discord.Colour.purple(),
    "dark_red": discord.Colour.dark_red(),
    "dark_blue": discord.Colour.dark_blue(),
    "dark_grey": discord.Colour.dark_grey()
}

PERM_PRESETS = {
    "admin": discord.Permissions.all(),
    "mod": discord.Permissions(
        kick_members=True,
        ban_members=True,
        manage_channels=True,
        manage_messages=True,
        moderate_members=True
    ),
    "basic": discord.Permissions(
        read_messages=True,
        send_messages=True,
        connect=True,
        speak=True
    )
}

# Configuración del bot
intents = discord.Intents.default()
intents.guilds = True
intents.guild_messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"\n{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Conectado como {Fore.YELLOW}{bot.user}")
    
    # Menú principal
    print(f"{Fore.CYAN}║ {Fore.WHITE}[{Fore.CYAN}1{Fore.WHITE}] Configuración Turbo (3 pasos)")                                                          
    print(f"{Fore.CYAN}║ {Fore.WHITE}[{Fore.CYAN}2{Fore.WHITE}] Configuración Avanzada Manual")                                                          
    print(f"{Fore.CYAN}║ {Fore.WHITE}[{Fore.CYAN}3{Fore.WHITE}] Configurar Webhooks (Redes Sociales)")
    print(f"{Fore.CYAN}║ {Fore.WHITE}[{Fore.CYAN}4{Fore.WHITE}] Personalización Avanzada de Roles  ") 

    
    option = get_input("Selecciona una opción")
    
    guild = bot.get_guild(guild_id)
    if not guild:
        print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] Servidor no encontrado")
        await bot.close()
        return
    
    if option == "1":
        config = await turbo_setup()
        await setup_turbo(guild, config)
    elif option == "2":
        await advanced_setup(guild)
    elif option == "3":
        await setup_webhooks(guild)
    elif option == "4":
        await role_customization(guild)
    
    await bot.close()

async def setup_turbo(guild, config):
    try:
        print(f"\n{Fore.WHITE}[{Fore.MAGENTA}⚡{Fore.WHITE}] Iniciando configuración turbo...")
        
        # Eliminar canales existentes
        await delete_existing(guild)
        
        # Aplicar plantilla
        template = TEMPLATES["gaming" if config["server_type"] == "1" else "empresa" if config["server_type"] == "2" else "gaming"]
        
        # Crear estructura
        print(f"\n{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Creando estructura turbo...")
        await create_structure(guild, template["estructura"], config["main_color"])
        
        # Crear roles
        print(f"\n{Fore.WHITE}[{Fore.BLUE}+{Fore.WHITE}] Configurando roles automáticos...")
        await create_roles(guild, template["roles"])
        
        print(f"\n{Fore.WHITE}[{Fore.GREEN}✓{Fore.WHITE}] Configuración turbo completada en {Fore.YELLOW}{len(guild.channels)} canales{Fore.WHITE} y {Fore.YELLOW}{len(guild.roles)} roles{Fore.WHITE}!")
        
    except Exception as e:
        print(f"\n{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] Error en turbo setup: {e}")

async def advanced_setup(guild):
    try:
        print(f"\n{Fore.WHITE}[{Fore.BLUE}*{Fore.WHITE}] Iniciando configuración avanzada...")
        
        # Eliminar canales existentes
        await delete_existing(guild)
        
        # Configuración personalizada
        estructura_personalizada = {}
        print(f"\n{Fore.WHITE}[{Fore.CYAN}i{Fore.WHITE}] Configuración de categorías (deja vacío para terminar)")
        
        while True:
            nombre_categoria = get_input("Nombre de la categoría")
            if not nombre_categoria:
                break
                
            canales = []
            print(f"{Fore.WHITE}[{Fore.CYAN}i{Fore.WHITE}] Añade canales para {Fore.YELLOW}{nombre_categoria}{Fore.WHITE} (deja vacío para terminar)")
            while True:
                nombre_canal = get_input("Nombre del canal")
                if not nombre_canal:
                    break
                canales.append(nombre_canal)
            
            estructura_personalizada[nombre_categoria] = canales
        
        # Crear estructura personalizada
        await create_structure(guild, estructura_personalizada)
        
        print(f"\n{Fore.WHITE}[{Fore.GREEN}✓{Fore.WHITE}] Configuración avanzada completada!")
        
    except Exception as e:
        print(f"\n{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] Error en configuración avanzada: {e}")

async def setup_webhooks(guild):
    try:
        print(f"\n{Fore.WHITE}[{Fore.MAGENTA}🌐{Fore.WHITE}] Configurando webhooks para redes sociales...")
        
        # Crear categoría si no existe
        categoria = discord.utils.get(guild.categories, name="📡・REDES SOCIALES")
        if not categoria:
            categoria = await guild.create_category("📡・REDES SOCIALES")
            print(f"{Fore.WHITE}  {Fore.GREEN}+{Fore.WHITE} Categoría creada: 📡・REDES SOCIALES")
        
        # Twitter Webhook
        twitter_channel = await guild.create_text_channel("🐦・twitter", category=categoria)
        webhook = await twitter_channel.create_webhook(name="Twitter Feed")
        print(f"{Fore.WHITE}  {Fore.BLUE}↳{Fore.WHITE} Webhook Twitter creado: {webhook.url}")
        
        # YouTube Webhook
        yt_channel = await guild.create_text_channel("📺・youtube", category=categoria)
        webhook = await yt_channel.create_webhook(name="YouTube Feed")
        print(f"{Fore.WHITE}  {Fore.BLUE}↳{Fore.WHITE} Webhook YouTube creado: {webhook.url}")
        
        print(f"\n{Fore.WHITE}[{Fore.GREEN}✓{Fore.WHITE}] Webhooks configurados correctamente!")
        print(f"{Fore.WHITE}[{Fore.CYAN}i{Fore.WHITE}] Configura estos webhooks en IFTTT o Zapier para automatización")
        
    except Exception as e:
        print(f"\n{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] Error configurando webhooks: {e}")

async def role_customization(guild):
    try:
        print(f"\n{Fore.WHITE}[{Fore.YELLOW}👑{Fore.WHITE}] Personalización avanzada de roles")
        
        roles_config = {}
        print(f"{Fore.WHITE}[{Fore.CYAN}i{Fore.WHITE}] Configura los roles (deja vacío el nombre para terminar)")
        
        while True:
            nombre_rol = get_input("Nombre del rol")
            if not nombre_rol:
                break
                
            color = get_input(f"Color para {nombre_rol} ({'/'.join(COLOR_MAP.keys())})")
            permisos = get_input(f"Tipo de permisos ({'/'.join(PERM_PRESETS.keys())})")
            
            roles_config[nombre_rol] = {
                "color": color,
                "perms": permisos
            }
        
        # Crear roles
        await create_roles(guild, roles_config)
        
        print(f"\n{Fore.WHITE}[{Fore.GREEN}✓{Fore.WHITE}] Roles personalizados creados exitosamente!")
        
    except Exception as e:
        print(f"\n{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] Error en personalización de roles: {e}")

async def delete_existing(guild):
    print(f"{Fore.WHITE}[{Fore.RED}-{Fore.WHITE}] Eliminando canales existentes...")
    for channel in guild.channels:
        try:
            await channel.delete()
            await asyncio.sleep(0.5)
        except:
            pass
            
    print(f"{Fore.WHITE}[{Fore.RED}-{Fore.WHITE}] Eliminando roles existentes...")
    for role in guild.roles:
        try:
            if role.name != "@everyone":
                await role.delete()
                await asyncio.sleep(0.5)
        except:
            pass

async def create_structure(guild, estructura, color_theme=None):
    for nombre_categoria, canales in estructura.items():
        try:
            # Aplicar estilo de color si hay tema
            if color_theme and color_theme in ["red", "blue", "green", "morado"]:
                nombre_categoria = nombre_categoria.replace("・", f"・{color_theme.upper()}・")
                
            categoria = await guild.create_category(nombre_categoria)
            print(f"\n{Fore.WHITE}  {Fore.CYAN}≡{Fore.WHITE} Categoría creada: {nombre_categoria}")
            
            for nombre_canal in canales:
                try:
                    if color_theme:
                        nombre_canal = nombre_canal.replace("・", f"・{color_theme[0].upper()}・")
                    await guild.create_text_channel(nombre_canal, category=categoria)
                    print(f"{Fore.WHITE}    {Fore.GREEN}↳{Fore.WHITE} Canal creado: {nombre_canal}")
                    await asyncio.sleep(0.5)
                except Exception as e:
                    print(f"{Fore.WHITE}    {Fore.RED}!{Fore.WHITE} Error al crear canal {nombre_canal}: {e}")
        except Exception as e:
            print(f"{Fore.WHITE}  {Fore.RED}!{Fore.WHITE} Error al crear categoría {nombre_categoria}: {e}")

async def create_roles(guild, roles_config):
    for nombre_rol, config in roles_config.items():
        try:
            color = COLOR_MAP.get(config["color"], discord.Colour.default())
            permissions = PERM_PRESETS.get(config["perms"], discord.Permissions.none())
            
            await guild.create_role(
                name=nombre_rol,
                colour=color,
                permissions=permissions
            )
            print(f"{Fore.WHITE}  {Fore.GREEN}+{Fore.WHITE} Rol creado: {nombre_rol} ({config['color']})")
            await asyncio.sleep(0.5)
        except Exception as e:
            print(f"{Fore.WHITE}  {Fore.RED}!{Fore.WHITE} Error al crear rol {nombre_rol}: {e}")

# Iniciar bot
token = get_input("Token del bot")
guild_id = int(get_input("ID del servidor"))

bot.run(token)
