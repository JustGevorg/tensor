from selenium.webdriver.common.by import By

from src.consts import KAMCHATKA_REGION


class BaseLocators:
    PARENT_LOCATOR = (By.XPATH, "..")
    COOKIE_AGREEMENT_CLOSE_CROSS = (By.CLASS_NAME, "tensor_ru-CookieAgreement__close")


class SbisPageLocators(BaseLocators):
    CONTACTS_PAGE_LINK = (By.LINK_TEXT, "Контакты")

    REGION_DEFINED = (
        By.XPATH,
        "(//span[@class='sbis_ru-Region-Chooser__text sbis_ru-link'])[1]",
    )
    PARTNERS_LIST = (
        By.XPATH,
        "(//div[@name='itemsContainer' and @data-qa='items-container'])[1]/div[position()>1]",
    )
    KAMCHATKA_REGION_ITEM = (By.XPATH, f"//span[@title='{KAMCHATKA_REGION}']")


class TensorPageLocators(BaseLocators):
    TENSOR_BANNER_IMG = (
        By.XPATH,
        "//img[@alt='Разработчик системы СБИС — компания «Тензор»']",
    )
    STRENGTH_IS_IN_PEOPLE_BLOCK = (
        By.XPATH,
        "//p[text()='Сила в людях']",
    )
    STRENGTH_IS_IN_PEOPLE_ABOUT = (By.LINK_TEXT, "Подробнее")
    WORKING_BLOCK = (
        By.XPATH,
        "//*[contains(@class, 'tensor_ru-container') and contains (*//text(), 'Работаем')]",
    )
    WORKING_BLOCK_IMAGE = (By.TAG_NAME, "img")
