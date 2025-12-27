from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SeleniumEngine:
    def __init__(self, timeout=30):
        options = Options()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, timeout)

    def open(self, url):
        self.driver.get(url)

    def click(self, selector):
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
        ).click()

    def type(self, selector, value):
        el = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        )
        el.clear()
        el.send_keys(value)

    def wait_for_selector(self, selector):
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        )

    def wait_seconds(self, seconds):
        time.sleep(seconds)

    def quit(self):
        self.driver.quit()
