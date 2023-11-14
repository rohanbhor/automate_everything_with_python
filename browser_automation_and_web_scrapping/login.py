from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage") # Avoid issue on launching browser on linux
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options)
    driver.implicitly_wait(20)
    driver.get("http://automated.pythonanywhere.com/login")
    return driver

def clean_text(txt):
    return float(txt.split(":")[1])

def main():
    driver = get_driver()
    driver.find_element("id", "id_username").send_keys("automated")
    driver.find_element("id", "id_password").send_keys("automatedautomated")
    driver.find_element("xpath", "//button[contains(., 'Sign in')]").click()
    driver.find_element("xpath", "//a[contains(., 'Home')]").click()

    now = time.time()
    max_time = now + 20
    while time.time() < max_time :
        avg_temp = driver.find_element("xpath", "//h1[@id='displaytimer']/div").text

        dt = datetime.strftime(datetime.now(), "%Y-%m-%d-%H-%M-%S")
        with open(f'{dt}.txt', 'w') as f:
            f.write(str(clean_text(avg_temp)))

        time.sleep(2)


if __name__ == '__main__':
    main()

