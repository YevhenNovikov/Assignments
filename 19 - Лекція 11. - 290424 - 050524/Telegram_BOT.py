
import requests
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackContext

API_KEY = 'A6N6ATguhkSqV6ohQmVr3Ip6x3GwkAxT'
TOKEN = '7067774416:AAEWKgUHoyhi2C0QcG1KBPsqdgEyv3PsO-Q'
BOT_USERNAME: Final = '@GIF_Labrador_bot'

def search_gifs(search_term: str):
    base_url = 'https://api.giphy.com/v1/'
    endpoint = 'gifs/search'
    URL = f"{base_url}{endpoint}"
    PARAMS = {
        'api_key': API_KEY,
        'q': search_term,
        'limit': 5
    }

    response = requests.get(URL, params=PARAMS)
    
    if response.status_code == 200:
        data = response.json()
        gif_urls = [gif['url'] for gif in data['data']]
        return gif_urls
    else:
        return []

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Enter a word to search for GIF.')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Enter a word to search for GIFs using Giphy.')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command!')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    search_term = update.message.text
    gifs = search_gifs(search_term)
    
    if gifs:
        for gif_url in gifs:
            await update.message.reply_text(gif_url)
    else:
        await update.message.reply_text('No GIFs found for your search.')

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.add_error_handler(error)

    print('Polling...')
    app.run_polling(poll_interval=3)