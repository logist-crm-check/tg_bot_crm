import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
#import ephem
from config import tgtoken

logging.basicConfig(filename="bot.log", level=logging.INFO)

def greet_user(update, context):
    print("Вызван /start")
    update.message.reply_text("Привет, пользователь! Ты вызвал команду /start")

def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def main():
    mybot = Updater(tgtoken, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('template', send_template))

    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")

    mybot.start_polling()
    mybot.idle()

TEMPLATE_ONE="""ПРОВЕРКА
авто, водитель, ООО (ИП)
[удалите из перечня те объекты, которые не нужно проверять]
"""

def send_template(update, context):
    print("Пользователь запросил шаблон")
    update.message.reply_text("Держи шаблон")
    update.message.reply_text(TEMPLATE_ONE)

main()