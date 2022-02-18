import telebot
import parser
import auth_data
from telebot import types


def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Recent items')
        item2 = types.KeyboardButton('Collect data')
        item3 = types.KeyboardButton('Get data')

        markup.add(item1, item2, item3)

        bot.send_message(message.chat.id, "HI, {0.first_name}!".format(message.from_user), reply_markup=markup)

    @bot.message_handler(content_types=["text"])
    def send_text(message):
        if message.chat.type == 'private':
            if message.text == 'Recent items':
                bot.send_message(message.chat.id, parser.recent())

            elif message.text == 'Collect data':
                parser.collect()
                bot.send_message(message.chat.id, 'Succeed')

            elif message.text == 'Get data':
                bot.send_document(message.chat.id, open('project.txt', 'rb'))

        # bot.send_message(message.chat.id, "Hi, what's up?")

    bot.delete_webhook()
    bot.infinity_polling()


if __name__ == '__main__':
    parser.login(auth_data.user_email, auth_data.user_password)
    telegram_bot(auth_data.token)
