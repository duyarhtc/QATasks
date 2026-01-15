from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):

    URL = "https://insiderone.com/"
    TITLE = "Insider"

    HEADER = (By.TAG_NAME, "header")
    NAVIGATION = (By.TAG_NAME, "nav")
    HERO_TITLE = (By.TAG_NAME, "h1")
    FOOTER = (By.TAG_NAME, "footer")
    

    def load(self):
        super().load(self.URL, self.TITLE)
        self.close_cookie_banner()

    def verify_main_blocks_loaded(self):
        assert self.is_visible(self.HEADER), "Header not visible"
        print("Header visible")
        assert self.is_visible(self.NAVIGATION), "Navigation not visible"
        print("Navigation visible")
        assert self.is_visible(self.HERO_TITLE), "Hero section not visible"
        hero_text = self.get_text(self.HERO_TITLE)
        print(f"Hero Title visible  | Title: '{hero_text}'" )
        self.scroll_into_view(self. FOOTER)
        assert self.is_visible(self.FOOTER), "Footer not visible"
        print("Footer visible")