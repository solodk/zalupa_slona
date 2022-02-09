from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import auth_data

# service = Service("C:\\Users\\krabs\\Downloads\\govno_slona\\govno_slona\\chromedriver\\chromedriver.exe")
# use for windows
# chrome must be installed and version of chromedriver must be identical
service = Service('/home/ubuntu/Desktop/projects/zalupa_slona/chromedriver/chromedriver')
url = "https://care.service-now.com"
url2 = "https://care.service-now.com/task_list.do"
driver = webdriver.Chrome(service=service)

try:
    driver.get(url="https://skladbet.com/login")

    email_input = driver.find_element(By.NAME, "login")
    email_input.clear()
    email_input.send_keys(auth_data.user_email)

    password_input = driver.find_element(By.NAME, "password")
    password_input.clear()
    password_input.send_keys(auth_data.user_pasword)

    time.sleep(2)
    #
    # password_input.send_keys(Keys.ENTER)
    # time.sleep(1)
    #
    # driver.get(url2)
    # items = driver.find_elements(By.CLASS_NAME, "bbWrapper")
    # with open("project.txt", "w") as file:
    #     for i in range(0, len(items)):
    #         file.write(items[i].text)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()