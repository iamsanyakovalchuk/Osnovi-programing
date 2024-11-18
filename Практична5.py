import telebot

TOKEN = '7365236155:AAFMJmFGH6qhfBQNnk176_CP0Vz4KoZvEPc'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

bot.polling()