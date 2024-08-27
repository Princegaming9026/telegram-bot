from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Function to start the bot and send a welcome message
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    chat_id = update.effective_chat.id
    welcome_message = f"Hello {user.first_name}! Welcome to the bot.\nYour Chat ID is: {chat_id}"
    await update.message.reply_text(welcome_message)

def main():
    # Replace 'YOUR_BOT_TOKEN' with your actual Telegram Bot Token
    app = ApplicationBuilder().token("6197747448:AAFrgXeZdjQZ1iTm9AE6v56h6y-qShiH5es").build()

    # Register the start command
    app.add_handler(CommandHandler("start", start))

    # Start the bot
    app.run_polling()

if __name__ == '__main__':
    main()

