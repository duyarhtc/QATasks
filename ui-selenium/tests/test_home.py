from pages.home_page import HomePage


def test_home_and_careers(driver):
    home = HomePage(driver)
    home.load()
    home.verify_main_blocks_loaded()
    


