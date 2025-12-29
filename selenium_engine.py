from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException
import time
import os
import random
from pathlib import Path

class SeleniumEngine:
    def __init__(self, timeout=15, max_retries=3):
        self.max_retries = max_retries
        self.timeout = timeout
        
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-extensions")
        options.add_argument("--no-sandbox")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        
        self.driver = webdriver.Chrome(options=options)
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        self.wait = WebDriverWait(self.driver, timeout)

    def _retry_op(self, operation, *args, **kwargs):
        for attempt in range(self.max_retries):
            try:
                return operation(*args, **kwargs)
            except Exception as e:
                if attempt < self.max_retries - 1:
                    time.sleep(random.uniform(0.5, 1.5))
                else:
                    raise e

    def open(self, url): self._retry_op(lambda: (self.driver.get(url), time.sleep(2))[0])

    def click(self, selector):
        def _click():
            el = self._find_any(selector)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", el)
            time.sleep(0.3)
            self.driver.execute_script("arguments[0].click();", el)
        self._retry_op(_click, selector)

    def type(self, selector, value):
        def _type():
            el = self._find_any(selector)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", el)
            self.driver.execute_script("arguments[0].removeAttribute('readonly');", el)
            self.driver.execute_script("arguments[0].value = arguments[1];", el, value)
        self._retry_op(_type, selector, value)

    def _find_any(self, selector, timeout=5):
        strategies = [(By.CSS_SELECTOR, selector), (By.NAME, selector.split('=')[1])]
        for by, sel in strategies:
            try:
                return self.wait.until(EC.presence_of_element_located((by, sel)))
            except:
                continue
        return self.driver.find_element(By.CSS_SELECTOR, selector)

    def wait_for_selector(self, selector, timeout=10):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))

    def wait_seconds(self, seconds): time.sleep(seconds)

    def scroll_to_selector(self, selector):
        el = self._find_any(selector)
        self.driver.execute_script("arguments[0].scrollIntoView();", el)

    def scroll_pixels(self, pixels):
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")

    def hover(self, selector):
        el = self._find_any(selector)
        ActionChains(self.driver).move_to_element(el).perform()

    def double_click(self, selector):
        el = self._find_any(selector)
        ActionChains(self.driver).double_click(el).perform()

    def right_click(self, selector):
        el = self._find_any(selector)
        ActionChains(self.driver).context_click(el).perform()

    def drag_drop(self, source, target):
        s = self._find_any(source); t = self._find_any(target)
        ActionChains(self.driver).drag_and_drop(s, t).perform()

    def select_option(self, selector, option, method="text"):
        el = self._find_any(selector)
        Select(el).select_by_visible_text(option)

    def clear(self, selector):
        el = self._find_any(selector)
        self.driver.execute_script("arguments[0].value = '';", el)

    def screenshot(self, filename=None):
        if not filename: filename = f"screenshot_{int(time.time())}.png"
        Path("screenshots").mkdir(exist_ok=True)
        self.driver.save_screenshot(f"screenshots/{filename}")
        return f"screenshots/{filename}"

    def switch_window(self, window):
        if window == "next": self.driver.switch_to.window(self.driver.window_handles[-1])

    def back(self): self.driver.back()
    def forward(self): self.driver.forward()
    def refresh(self): self.driver.refresh()
    def close(self): self.driver.close()

    def get_text(self, selector):
        return self._find_any(selector).text

    def get_attribute(self, selector, attr):
        return self._find_any(selector).get_attribute(attr)

    def is_visible(self, selector):
        return self._find_any(selector).is_displayed()

    def quit(self):
        try: self.driver.quit()
        except: pass
