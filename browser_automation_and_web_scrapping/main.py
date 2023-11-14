from selenium import webdriver


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
    driver.get("http://automated.pythonanywhere.com")
    return driver

def clean_text(txt):
    return float(txt.split(":")[1])

def main():
    driver = get_driver()
    element1 = driver.find_element("xpath", "//h1[contains(@class, 'animated')]").text
    print(element1)

    element2 = driver.find_element("xpath", "//h1[@id='displaytimer']/div").text
    print(clean_text(element2))



if __name__ == '__main__':
    main()

