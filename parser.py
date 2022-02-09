from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# service = Service("C:\\Users\\krabs\\Downloads\\govno_slona\\govno_slona\\chromedriver\\chromedriver.exe")
# use for windows
service: Service = Service("chromedriver/chromedriver")
url = "https://care.service-now.com"
url2 = "https://care.service-now.com/task_list.do"
driver = webdriver.Chrome()

try:
    driver.get(url=url)

    email_input = driver.find_element(By.NAME, "user_name")
    email_input.clear()
    email_input.send_keys("test")

    password_input = driver.find_element(By.NAME, "user_password")
    password_input.clear()
    password_input.send_keys("test")

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