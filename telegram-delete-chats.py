# This script python delete all chats and only need telthon python and your api config
# Goto here https://my.telegram.org/apps   for get api config
#pip install telethon
from telethon.sync import TelegramClient

# Configuración de la API de Telegram
api_id = 'TU_API_ID'
api_hash = 'TU_API_HASH'
phone_number = 'TU_NUMERO_DE_TELEFONO'  # Ejemplo: '+34123456789'

# Inicializa el cliente de Telethon
client = TelegramClient('session_name', api_id, api_hash)

async def borrar_todos_los_chats():
    async with client:
        async for dialog in client.iter_dialogs():
            try:
                await client.delete_dialog(dialog.id)
                print(f"Chat con {dialog.name} borrado.")
            except Exception as e:
                print(f"No se pudo borrar el chat con {dialog.name}: {e}")

# Ejecuta la función para borrar todos los chats
with client:
    client.loop.run_until_complete(borrar_todos_los_chats())

