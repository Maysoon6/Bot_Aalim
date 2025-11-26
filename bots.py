import os
from telegram.ext import Application

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

app = Application.builder().token(TOKEN).build()

# أضف handlers للأوامر هنا
from telegram.ext import CommandHandler

async def start(update, context):
    await update.message.reply_text('مرحباً! البوت يعمل الآن 🎉')

app.add_handler(CommandHandler("start", start))

# التشغيل
print("البوت يبدأ التشغيل...")
app.run_polling()