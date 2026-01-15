from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class QAJobsPage(BasePage):

    URL = "https://insiderone.com/careers/quality-assurance/"
    TITLE= "Quality Assurance"

    # --- Locators ---
    SEE_ALL_JOBS_BTN = (By.XPATH, "//a[contains(text(),'See all QA jobs')]")
    LOCATION_FILTER = (By.ID, "filter-by-location")
    DEPARTMENT_FILTER= (By.ID, "filter-by-department")
    JOB_LIST_ITEMS = (By.CSS_SELECTOR, ".position-list-item")
    LAST_JOB_VIEW_BUTTON = (By.XPATH, "(//a[contains(text(),'View Role')])[last()]")


    def load(self):
        super().load(self.URL,self.TITLE)
        self.close_cookie_banner()
  

    def click_see_all_jobs(self):
        self.scroll_into_view(self.SEE_ALL_JOBS_BTN)
        self.wait_and_click(self.SEE_ALL_JOBS_BTN)
        time.sleep(10) # wait for uploding dropdown items

    def filter_by_location(self, location="Istanbul, Turkiye"):
        self.scroll_into_view(self.LOCATION_FILTER)
        self.focus(self.LOCATION_FILTER)
        time.sleep(0.5)
        self.wait_and_select(self.LOCATION_FILTER, location)
        self.select_from_dropdown(self.LOCATION_FILTER, location)
        time.sleep(2)

    def filter_by_department(self, department="Quality Assurance"):
        self.scroll_into_view(self.DEPARTMENT_FILTER)
        self.focus(self.DEPARTMENT_FILTER)
        time.sleep(0.5)
        self.wait_and_select(self.DEPARTMENT_FILTER , department)
        self.select_from_dropdown(self.DEPARTMENT_FILTER, department)
        time.sleep(2)

    
    def verify_job_list_exists(self, wait_time=10):
        try:
            jobs = WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_all_elements_located(self.JOB_LIST_ITEMS)
            )
            job_count = len(jobs)
            print(f"Job list loaded: {job_count} jobs found.")
            time.sleep(2)
            if job_count > 0:
                return jobs  
            else:
                return False  # if empty return false
        except:
            return False  
        
    def verify_job_list_visible(self):
       
        job_cards = self.driver.find_elements(*self.JOB_LIST_ITEMS)
        visible_cards = [card for card in job_cards if card.is_displayed()]

        if len(visible_cards) > 0:
            print(f"Visible job cards: {len(visible_cards)}")
            for card in job_cards:
                # hover ,Scroll ve focus
                self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center'});", card)
                self.driver.execute_script("arguments[0].focus();", card)
                ActionChains(self.driver).move_to_element(card).perform() 
                time.sleep(3)  
            return visible_cards  
        else:
            print("ERROR: Job cards exist but are not visible!")
            return False  
        
    def verify_job_details(self, expected_location="Istanbul, Turkiye", expected_department="Quality Assurance"):
        job_cards = self.driver.find_elements(*self.JOB_LIST_ITEMS)
        if not job_cards:
            print("No job cards found!")
            return False

        all_ok = True
        for index in range(len(job_cards)):
            try:
                # her seferinde güncel element al
                card = self.driver.find_elements(*self.JOB_LIST_ITEMS)[index]

                if not card.is_displayed():
                    continue

                title = card.find_element(By.CSS_SELECTOR, ".position-title").text
                location = card.find_element(By.CSS_SELECTOR, ".position-location").text
                department = card.find_element(By.CSS_SELECTOR, ".position-department").text

                print(f"Job {index+1}: {title} | {department} | {location}")

                if expected_location not in location:
                    print(f"ERROR: Job {index+1} location mismatch: {location}")
                    all_ok = False
                if expected_department not in department:
                    print(f"ERROR: Job {index+1} department mismatch: {department}")
                    all_ok = False
                if "Quality Assurance" not in title:
                    print(f"ERROR: Job {index+1} title mismatch: {title}")
                    all_ok = False

            except StaleElementReferenceException:
                print(f"WARNING: Job {index+1} went stale, retrying...")
                time.sleep(1)
                card = self.driver.find_elements(*self.JOB_LIST_ITEMS)[index]
        return True

    def click_last_job_view_role(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LAST_JOB_VIEW_BUTTON)
            )
        button.click()
        time.sleep(3) 
    
    
    
    def test_view_role_redirects_to_lever(self):
        try:
            self.driver.switch_to.window(self.driver.window_handles[-1])
            WebDriverWait(self.driver, 10).until(
                lambda d: "lever.co" in d.current_url.lower()
            )

            if "lever.co" in self.driver.current_url.lower():
                print("SUCCESS: Redirected to Lever Application page.")
                return True

            print(f"WARNING: URL  not Lever  → {self.driver.current_url}")
            return False

        except Exception as e:
            print(f"ERROR: Redirect check failed → {e}")
            return False
        
