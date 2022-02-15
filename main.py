import telebot
import parser
import auth_data
from telebot import types


def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        markup = telebot.types.ReplyKeyboardMarkup(True, False)
        markup.row('')
        bot.send_message(message.chat.id, "Welcome test msg")

    @bot.message_handler(content_types=["text"])
    def send_text(message):
        bot.send_message(message.chat.id, parser.recent())

    @bot.message_handler(commands=['button'])
    def button(message):
        markup = types.InlineKeyboardMarkup(row_width=1)
        item = types.InlineKeyboardButton('Показать последнее', callback_data='show_recent')
        markup.add(item)

        bot.send_message(message.chat.id, 'Выбери', reply_markup=markup)

    bot.delete_webhook()
    bot.infinity_polling()


if __name__ == '__main__':
    #telegram api blocked at work
    #telegram_bot(token)
    parser.login(auth_data.user_email, auth_data.user_password)
    #parser.collect()
    parser.recent()
    parser.close()
