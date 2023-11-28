import telebot
bot = telebot.TeleBot('6859947811:AAGq-HEJpKllYwZpM6GjDCzJER4mRyHojgQ')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'ты солнце <3')

bot.infinity_polling()