from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import funciones
import os
from dotenv import load_dotenv

# 🔑 Token del chat bot
load_dotenv()
TOKEN = os.getenv("token")

async def start(update:  Update, context: ContextTypes. DEFAULT_TYPE):
    await update.message.reply_text("¡Hola!  Soy tu bot de descargas de Twitter 🤖")

    # 🟢 Responder a cualquier mensaje de texto
"""async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensaje = update.message.text
    await update.message.reply_text(f"Recibí: {mensaje}")
"""

async def xtomp4(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text
    await update.message.reply_text("Procesando URL")
    await update.message.reply_text("Descargando")
    funciones.descargar_video(url)
    await update.message.reply_text("Video descargado, Enviado...")
    with open("video.mp4",'rb') as video_file:
        await update.message.reply_video(video=video_file)
    print ("Borrando Archivo")
    os.remove("video.mp4")

# 🚀 Función principal
def main():
    # Crear la aplicación
    app = Application.builder().token(TOKEN).build()
    
    # Registrar handlers (como las rutas de Flask)
    app.add_handler(CommandHandler("start", start))
    #app.add_handler(MessageHandler(filters. TEXT & ~filters.COMMAND, echo))
    app.add_handler(MessageHandler(filters. TEXT & ~filters.COMMAND, xtomp4))

    # Iniciar el bot
    print("🤖 Bot iniciado...")
    app.run_polling()

    

if __name__ == '__main__':
    main()

