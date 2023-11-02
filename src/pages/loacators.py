from selenium.webdriver.common.by import By


class BaseLocators:
    PARENT_LOCATOR = (By.XPATH, "..")


class SbisPageLocators(BaseLocators):
    CONTACTS_PAGE_LINK = (By.LINK_TEXT, "Контакты")
    TENSOR_BANNER_IMG = (
        By.XPATH,
        "//img[@alt='Разработчик системы СБИС — компания «Тензор»']",
    )
    STRENGTH_IS_IN_PEOPLE_BLOCK = (
        By.XPATH,
        "//p[text()='Сила в людях']",
    )
    STRENGTH_IS_IN_PEOPLE_ABOUT = (By.LINK_TEXT, "Подробнее")
    COOKIE_AGREEMENT_CLOSE_CROSS = (By.CLASS_NAME, "tensor_ru-CookieAgreement__close")
    WORKING_BLOCK = (
        By.XPATH,
        "//*[contains(@class, 'tensor_ru-container') and contains (*//text(), 'Работаем')]",
    )
    WORKING_BLOCK_IMAGE = (By.TAG_NAME, "img")
    REGION_DEFINED = (By.CLASS_NAME, "sbis_ru-Region-Chooser__text sbis_ru-link")
