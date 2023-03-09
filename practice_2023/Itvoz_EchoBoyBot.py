import telebot

TOKEN = "5866957629:AAGDq8FDrVVlyZWrdu8UNKM9WX2I6xBBgFU"

bot = telebot.TeleBot(TOKEN)


# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.send_message(message.chat.id, 'Команда')


# Обрабатывается все документы и аудиозаписи
@bot.message_handler(content_types=['document', 'audio', 'text', 'voice'])
def handle_docs_audio(message):
    bot.send_message(message.chat.id, 'Ответ')


@bot.message_handler(content_types=['photo'])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD')


bot.polling(none_stop=True)
