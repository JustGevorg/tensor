import time

from src.consts import SBIS_PAGE_URL
from src.pages.loacators import SbisPageLocators
from src.pages.page import SbisPage


def test_first_scenario(browser):
    sbis_page = SbisPage(driver=browser, base_url=SBIS_PAGE_URL)
    sbis_page.open_page()
    sbis_page.go_to_contacts_page(locator=SbisPageLocators.CONTACTS_PAGE_LINK)
    sbis_page.go_to_tensor_page(locator=SbisPageLocators.TENSOR_BANNER_IMG)
    time.sleep(1)


# def main() -> None:
#     ...


# if __name__ == "__main__":
#     main()
