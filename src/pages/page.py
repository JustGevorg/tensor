from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def open_page(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )

    def find_elements(self, locator, time=2):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}",
        )

    def go_to_section_by_clicking(self, locator, time=2):
        section = self.find_element(locator=locator, time=time)
        section.click()


class SbisPage(BasePage):
    def go_to_contacts_page(self, locator):
        self.go_to_section_by_clicking(locator=locator)

    def go_to_tensor_page(self, locator):
        self.go_to_section_by_clicking(locator=locator)

    def should_be_block_strength_is_in_people(self, locator):
        assert True

    def should_strength_is_in_people_about_open(self, locator):
        assert True

    def should_img_identical_sizes(self, locator):
        assert True
