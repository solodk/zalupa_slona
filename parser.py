from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import auth_data
# service = Service("C:\\Users\\krabs\\Downloads\\govno_slona\\govno_slona\\chromedriver\\chromedriver.exe")
# use for windows
# chrome must be installed and version of chromedriver must be identical
service = Service('/home/ubuntu/Desktop/projects/zalupa_slona/chromedriver/chromedriver')
chrome_options = Options()
#chrome_options.add_argument("--headless")
#chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(service=service, options=chrome_options)
logged = False
on_page = False

try:
    while not logged:
        driver.get(url="https://skladbet.com/login")

        email_input = driver.find_element(By.NAME, "login")
        email_input.clear()
        email_input.send_keys(auth_data.user_email)

        password_input = driver.find_element(By.NAME, "password")
        password_input.clear()
        password_input.send_keys(auth_data.user_pasword)

        password_input.send_keys(Keys.ENTER)
        time.sleep(1)
        logged = True

    if logged and not on_page:
        for i in range(62):
            driver.get(url="https://skladbet.com/forums/platnye-prognozy-besplatno.41/?prefix_id=19")
            page_url = driver.find_elements(By.CSS_SELECTOR, "[data-xf-init='preview-tooltip']")
            time.sleep(1)
            for k in range(len(page_url)):
                page_url[k].send_keys(Keys.ENTER)
                items = driver.find_elements(By.CLASS_NAME, "bbWrapper")
                with open("project.txt", "a") as file:
                    for u in range(0, (len(items) - 1)):
                        file.write(items[u].text)
                        print(u)
                driver.back()
                page_url = driver.find_elements(By.CSS_SELECTOR, "[data-xf-init='preview-tooltip']")
            # page = driver.find_element(By.CLASS, pageNav-page pageNav-page--later")
            # time.sleep(1)
            # page.send_keys(Keys.ENeTER)



except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
