from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os

TOKEN = os.getenv("TELEGRAM_TOKEN")  # Read token from environment variable

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to IntelliKiosk! Send me a product name or an image.")

async def handle_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]
    file = await context.bot.get_file(photo.file_id)
    file_path = await file.download_to_drive()

    # TODO: Replace this with actual prediction logic (Colab URL call)
    product_name = "detected_product"
    await update.message.reply_text(f"🖼️ Detected product: {product_name}")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.PHOTO, handle_image))

app.run_polling()
