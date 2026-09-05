from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

options = Options()
options.add_argument('start-maximized')

driver = webdriver.Chrome(options=options)
# driver.get('https://www.wildberries.ru/')
driver.get('https://www.bookvoed.ru/?ysclid=m4qvpnx1mv675804374')

time.sleep(5)
input = driver.find_element(By.XPATH, "//input[@class = 'search-form__input search-form__input--search']")
input.send_keys("хоккинг")
input.send_keys(Keys.ENTER)

time.sleep(20)

while True:
    # wait = WebDriverWait(driver, 30)
    # cards = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@data-product-id]")))
    while True:
        wait = WebDriverWait(driver, 30)
        cards = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@data-product-id]")))
        # cards = driver.find_elements(By.XPATH, "//div[@data-product-id]")
        print(len(cards))
        count = len(cards)
        driver.execute_script("window.scrollBy(0,2000)")
        time.sleep(2)
        cards = driver.find_elements(By.XPATH, "//div[@data-product-id]")
        if len(cards) == count:
            break

    for card in cards:
        name = card.find_element(By.XPATH, '//a[contains(@class, "ui-link ui-link__color-scheme--two")]').text
        url = card.find_element(By.XPATH, './div/a').get_attribute('href')
        print(name, url)

    try:
        button = driver.find_element(By.CLASS_NAME, 'base-link--active')
        actions = ActionChains(driver)
        actions.move_to_element(button).click()
        actions.perform()
    except:
        break

print()
