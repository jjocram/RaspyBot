import requests
import telegram
from telegram.ext import Updater, CommandHandler

from os import environ, popen
from sys import exit


def get_ip(bot, update):
    ip = requests.get('http://ifconfig.me').text
    update.message.reply_text(ip)

def get_temp(bot, update):
    update.message.reply_text(popen("vcgencmd measure_temp").read())


def get_uptime(bot, update):
    update.message.reply_text(popen("uptime").read())

def main():
    if "BOT_TOKEN" not in environ:
        print("BOT_TOKEN not found in environ")
        exit(2)

    TOKEN = environ["BOT_TOKEN"]
    updater = Updater(TOKEN)
    bot = telegram.Bot(TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('get_ip', get_ip))
    dp.add_handler(CommandHandler('get_temp', get_temp))
    dp.add_handler(CommandHandler('uptime', get_uptime))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
