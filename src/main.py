from src.consts import MY_REGION, SBIS_PAGE_URL
from src.pages.loacators import SbisPageLocators, TensorPageLocators
from src.pages.page import SbisPage


def test_first_scenario(browser):
    sbis_page = SbisPage(driver=browser, base_url=SBIS_PAGE_URL)
    sbis_page.open_page()
    sbis_page.go_to_contacts_page(locator=SbisPageLocators.CONTACTS_PAGE_LINK)
    sbis_page.go_to_tensor_page(locator=TensorPageLocators.TENSOR_BANNER_IMG)
    sbis_page.should_block_strength_is_in_people(
        locator=TensorPageLocators.STRENGTH_IS_IN_PEOPLE_BLOCK
    )
    sbis_page.should_strength_is_in_people_about_open(
        locator=TensorPageLocators.STRENGTH_IS_IN_PEOPLE_ABOUT
    )
    sbis_page.should_img_identical_sizes(locator=TensorPageLocators.WORKING_BLOCK)


def test_second_scenario(browser):
    sbis_page = SbisPage(driver=browser, base_url=SBIS_PAGE_URL)
    sbis_page.open_page()
    sbis_page.go_to_contacts_page(locator=SbisPageLocators.CONTACTS_PAGE_LINK)
    sbis_page.should_my_region_defined(
        locator=SbisPageLocators.REGION_DEFINED, my_region=MY_REGION
    )

    regions_partners = {MY_REGION: []}
    regions_partners[MY_REGION] = sbis_page.should_my_region_partners_list_exists(
        locator=SbisPageLocators.PARTNERS_LIST
    )
    sbis_page.choose_kamchatka_region(locator=SbisPageLocators.KAMCHATKA_REGION_ITEM)
    sbis_page.should_region_changes_applied(
        my_region_partners=regions_partners[MY_REGION]
    )
