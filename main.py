import telebot
#import parser
#import selenium
from auth_data import token

def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(message.chat.id, "Welcome test msg")

    @bot.message_handler(content_types=["text"])
    def send_text(message):
        bot.send_message(message.chat.id, "second test output")

    bot.delete_webhook()
    bot.infinity_polling()


if __name__ == '__main__':
    telegram_bot(token)