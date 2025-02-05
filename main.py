import telebot
import ismlar

TOKEN = "7121440092:AAEykdaNrTNbh5goUKTItBBazuDTHEYgTGY"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom! Men oddiy Telegram botman.")

@bot.message_handler(func=lambda msg: True)
def echo(message):
    ism = message.text
    javob = ism.title() + ' ismining manosi: \n' + ismlar.ism_manosi(ism)
    bot.reply_to(message, javob)
bot.polling()
