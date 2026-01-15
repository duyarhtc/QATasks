from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.support.ui import Select

class BasePage:

    def __init__(self, driver,timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self._timeout = timeout

    #####load all pages
    def load(self, url, title_contains):
        self.driver.get(url)
        print("Page opened, title:", self.driver.title)
        try:
                WebDriverWait(self.driver, 10).until(
                EC.title_contains(title_contains)
            )
                print("Title check passed:", self.driver.title)
        except TimeoutException:
                print("title is not suitable:", self.driver.title)
    
    ########close cookie banner 
    def close_cookie_banner(self):
        try:
            accept_btn = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.ID, "wt-cli-accept-all-btn"))
            )
            accept_btn.click()
            print("Cookie banner closed")
        except:
            print("Cookie banner displayed, pass")  

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()


    def wait_and_click(self, locator, timeout=10): #for see all button
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            element.click()
        except TimeoutException:
            print(f"Element {locator} can not click")
            raise
    def wait_and_select(self, locator,visible_text, timeout=10): # for filters 
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            select = Select(element)
            select.select_by_visible_text(visible_text)
        except TimeoutException:
            print(f"Element {locator} can not select")
            raise
    def get_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def is_visible(self, locator):
        return self.get_element(locator).is_displayed()
    

    def open(self, url):
        self.driver.get(url)

    
    ### scroll page
    def scroll_into_view(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        return element
    
    ### element focus
    def focus(self, locator): 
        element = self.driver.find_element(*locator)
        try:
            ActionChains(self.driver).move_to_element(element).perform()
        except:
            pass  
        self.driver.execute_script("arguments[0].focus();", element)
        return element
    
    ### scroll in dropdown
    
    def select_from_dropdown(self, dropdown_locator, option_text, wait_time=10):
       
            # <select> elementini bekle
        dropdown_element = WebDriverWait(self.driver, wait_time).until(
            EC.visibility_of_element_located(dropdown_locator)
        )
        # Select objesi ile visible text seç
        select = Select(dropdown_element)
        select.select_by_visible_text(option_text)
        print(f"Selected '{option_text}' from dropdown")

 
