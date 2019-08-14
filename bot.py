import requests
import telegram
from telegram.ext import Updater, CommandHandler

from os import environ
from sys import exit


def get_ip(bot, update):
    ip = requests.get('http://ifconfig.me').text
    update.message.reply_text(ip)

def main():
    if "BOT_TOKEN" not in environ:
        print("BOT_TOKEN not found in environ")
        exit(1)

    TOKEN = environ["BOT_TOKEN"]
    updater = Updater(TOKEN)
    bot = telegram.Bot(TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('get_ip', get_ip))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
