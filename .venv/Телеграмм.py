import telebot

TOKEN = "8474022805:AAEQQ_Z3OkfgKpVqfjZq7VLbfGfEU1fP7G0"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['photo'])
def send_photo(message:telebot.types.Message):
    bot.reply_to(message,"Ебать смехуятина шеф")
    pass

bot.polling(none_stop=True)
