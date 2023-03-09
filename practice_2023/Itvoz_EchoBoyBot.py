import telebot

TOKEN = "5866957629:AAGDq8FDrVVlyZWrdu8UNKM9WX2I6xBBgFU"

bot = telebot.TeleBot(TOKEN)
# bot.polling(none_stop=True)

# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    pass


# Обрабатывается все документы и аудиозаписи
@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
    pass
