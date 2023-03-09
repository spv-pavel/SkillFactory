import telebot

TOKEN = "5866957629:AAGDq8FDrVVlyZWrdu8UNKM9WX2I6xBBgFU"

bot = telebot.TeleBot(TOKEN)
bot.polling(none_stop=True)
