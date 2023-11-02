from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.consts import TENSOR_ABOUT_URL
from src.pages.loacators import SbisPageLocators


class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def open_page(self, url=None):
        if not url:
            return self.driver.get(self.base_url)
        return self.driver.get(url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}",
        )

    def go_to_section_by_clicking(self, locator, time=10):
        section = self.find_element(locator=locator, time=time)
        section.click()


class SbisPage(BasePage):
    def _remove_cookie_agrement(
        self, locator=SbisPageLocators.COOKIE_AGREEMENT_CLOSE_CROSS
    ):
        agreement_close_cross = self.find_element(locator=locator)
        agreement_close_cross.click()

    def go_to_contacts_page(self, locator):
        self.go_to_section_by_clicking(locator=locator, time=2)

    def go_to_tensor_page(self, locator):
        tensor_page_img = self.find_element(locator=locator)
        tensor_page_link = tensor_page_img.find_element(
            *SbisPageLocators.PARENT_LOCATOR
        ).get_attribute("href")
        self.open_page(url=tensor_page_link)

    def should_block_strength_is_in_people(self, locator):
        self._remove_cookie_agrement(
            locator=SbisPageLocators.COOKIE_AGREEMENT_CLOSE_CROSS
        )
        assert "Сила в людях" in self.find_element(
            locator=locator, time=10
        ).get_attribute("innerText")

    def should_strength_is_in_people_about_open(self, locator):
        block_strength_is_in_people_about = self.find_elements(
            locator=locator, time=15
        )[2]
        block_strength_is_in_people_about.click()
        assert TENSOR_ABOUT_URL == self.driver.current_url

    def should_img_identical_sizes(self, locator):
        working_block = self.find_element(locator=locator)
        images = working_block.find_elements(
            *SbisPageLocators.WORKING_BLOCK_IMAGE
        )  # implement via self.find_elements
        images_sizes = [
            (img.get_attribute("width"), img.get_attribute("height")) for img in images
        ]

        assert len(set(images_sizes)) == 1

    def should_my_region_defined(self, locator, my_region):
        defined_region = self.find_element(locator=locator).get_attribute("innerText")
        assert defined_region == my_region
        self.go_to_section_by_clicking(locator=locator)
