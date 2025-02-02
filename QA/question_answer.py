import telebot
from typing import Final 

TOKEN = '7579965998:AAFMTKhdrRCkY5pDaVV_4Y4NmvTwJTwVmdo'
bot = telebot.TeleBot(TOKEN) # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")
      
# Responses
def handle_response(message_text):

    if 'hello' in message_text.lower():
        return 'hi'
    
    if 'how are you' in message_text.lower():
        return 'I am good!'

    if 'I love python' in message_text.lower():
        return 'Remember to learn it!'

    return 'I do not understand what you wrote.'

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    response = handle_response(message.text)
    bot.reply_to(message, response)

bot.infinity_polling()
