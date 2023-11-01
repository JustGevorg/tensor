from selenium.webdriver.common.by import By


class SbisPageLocators:
    # HEADER_MENU = (
    #     By.CLASS_NAME,
    #     "sbisru-Header__menu ws-flexbox ws-align-items-center",
    # )
    # CONTACTS_PAGE_LINK = (By.CLASS_NAME, "sbisru-Header__menu-link")
    CONTACTS_PAGE_LINK = (By.LINK_TEXT, "Контакты")
    TENSOR_BANNER_IMG = (
        By.XPATH,
        "//img[@alt='Разработчик системы СБИС — компания «Тензор»']",
    )
    STRENGTH_IS_IN_PEOPLE_BLOCK = (By.CLASS_NAME, "tensor_ru-Index__block4-content")
