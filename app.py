from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

users = {
    "32149717": {
        "first_name": "Yigit Guler"
    }
}

updater = Updater('')
dispatcher = updater.dispatcher

def start(bot, update, args):
    user_id = update.message.from_user.id
    print user_id

    if user_id not in users.keys():
        if len(args) == 0:
            update.message.reply_text(
            u'Hello {first_name}, let\'s know each other better. ' \
            u'Please enter the secret key in following format: /start your-secret-key'.format(
                first_name=update.message.from_user.first_name
            ))
        else:
            if args[0] == "":
                print("success")
            else:
                update.message.reply_text("Wrong secret key.")


    update.message.reply_text(
        u'Hello {}'.format(update.message.from_user.first_name))

start_handler = CommandHandler('start', start, pass_args=True)
dispatcher.add_handler(start_handler)



def hello(bot, update):
    print update
    update.message.reply_text(
        u'Hello {}'.format(update.message.from_user.first_name))

def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)



echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)


updater.start_polling()
updater.idle()
