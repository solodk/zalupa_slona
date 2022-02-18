from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# service = Service("C:\\Users\\krabs\\Downloads\\govno_slona\\govno_slona\\chromedriver\\chromedriver.exe")
# use for windows
# chrome must be installed and version of chromedriver must be identical
service = Service('chromedriver/chromedriver')
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(service=service, options=chrome_options)


def login(email, password):
    driver.get(url="https://skladbet.com/login")

    email_input = driver.find_element(By.NAME, "login")
    email_input.clear()
    email_input.send_keys(email)

    password_input = driver.find_element(By.NAME, "password")
    password_input.clear()
    password_input.send_keys(password)

    password_input.send_keys(Keys.ENTER)

    print('login passed')

def collect():
    for i in range(1, 61):

        driver.get(url=f"https://skladbet.com/forums/platnye-prognozy-besplatno.41/page-{i}?prefix_id=19")
        main_page = driver.find_elements(By.CSS_SELECTOR, "[data-xf-init='preview-tooltip']")

        for k in range(len(main_page)):

            main_page = driver.find_elements(By.CSS_SELECTOR, "[data-xf-init='preview-tooltip']")
            main_page[k].send_keys(Keys.ENTER)

            items = driver.find_elements(By.CLASS_NAME, "bbWrapper")

            with open("project.txt", "a") as file:
                for u in range(0, (len(items) - 1)):
                    file.write(items[u].text)

                driver.back()


def recent():
    driver.get(url="https://skladbet.com/forums/platnye-prognozy-besplatno.41/?prefix_id=19")
    main_page = driver.find_element(By.CSS_SELECTOR, "[data-xf-init='preview-tooltip']").click()
    recent_item = driver.find_element(By.CLASS_NAME, "bbWrapper")
    return recent_item


def close():
    driver.close()
    driver.quit()
