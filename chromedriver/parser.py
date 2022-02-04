from auth_data import bet_pass
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# service=Service("/home/ubuntu/PycharmProjects/govno_slona/chromedriver/chromedriver")
service = Service("C:\\Users\\krabs\\Downloads\\govno_slona\\govno_slona\\chromedriver\\chromedriver.exe")
url = "https://skladbet.com/login/"
url2 = "https://skladbet.com/threads/26-10-21.5338/"
driver = webdriver.Chrome(service=service)

try:
    driver.get(url=url)

    email_input = driver.find_element(By.NAME, "login")
    email_input.clear()
    email_input.send_keys("scrambletoe@gmail.com")

    password_input = driver.find_element(By.NAME, "password")
    password_input.clear()
    password_input.send_keys(bet_pass)

    password_input.send_keys(Keys.ENTER)
    time.sleep(1)

    driver.get(url2)
    items = driver.find_elements(By.CLASS_NAME, "bbWrapper")
    with open("project.txt", "w") as file:
        for i in range(0, len(items)):
            file.write(items[i].text)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()