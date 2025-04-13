import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# توکن رو از متغیر محیطی می‌گیریم (برای امنیت در Render)
TOKEN = os.environ.get("7613253370:AAGO8W_NzE4kANB5TGLMUeSj6pvJ5wzBgkQ")

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[
        InlineKeyboardButton(
            text="باز کردن وب‌سایت",
            web_app=WebAppInfo(url="https://bohran-site.vercel.app")
        )
    ]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("روی دکمه زیر کلیک کن تا سایت باز بشه داخل تلگرام:", reply_markup=reply_markup)

# main function
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
