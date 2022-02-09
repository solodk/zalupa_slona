import telebot
from auth_data import token
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

service = Service("./chromedriver")
#service = Service("C:\\Users\\krabs\\Downloads\\govno_slona\\govno_slona\\chromedriver\\chromedriver.exe")
url = "https://care.service-now.com/"
#url2 = "https://care.service-now.com/task_list.do"
#driver = webdriver.Chrome(service=service)

def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(message.chat.id, "Welcome Test Output msg")

    # @bot.message_handler(content_types=["text"])
    # def send_text(message):
    #     login = False
    #     while message.text == "Ukraina matu":
    #         try:
    #             while not login:
    #                 driver.get(url=url)
    #
    #                 email_input = driver.find_element(By.NAME, "login")
    #                 email_input.clear()
    #                 email_input.send_keys("telebot@gmail.com")
    #
    #                 password_input = driver.find_element(By.NAME, "password")
    #                 password_input.clear()
    #                 password_input.send_keys(bet_pass)
    #
    #                 password_input.send_keys(Keys.ENTER)
    #                 time.sleep(1)
    #                 login = True
    #
    #             driver.get(url2)
    #             items = driver.find_elements(By.CLASS_NAME, "bbWrapper")
    #
    #             # with open("project.txt", "w") as file:
    #             #     for i in range(0, len(items)):
    #             #         file.write(items[i].text)
    #
    #             for i in range(0, len(items)):
    #                 bot.send_message(message.chat.id, items[i].text)
    #             time.sleep(30)
    #         except Exception as ex:
    #             print(ex)
    #             bot.send_message(message.chat.id, "Pomulka")
    #
    #     else:
    #         bot.send_message(message.chat.id, "Moskal?")

    bot.infinity_polling()


if __name__ == '__main__':
    # parser()
    telegram_bot(token)
