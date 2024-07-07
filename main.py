from dotenv import load_dotenv
import os
from telebot import TeleBot

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello, World!')
    

if __name__ == '__main__':
    bot.infinity_polling()
