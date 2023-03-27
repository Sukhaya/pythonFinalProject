import time

from pages.BasePage import BasePage

from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    PAGE_TITLE = (By.XPATH, "//h1")
    BUTTON_ADD_TO_CART = (By.XPATH, "//button[contains(text(), 'В корзину')]")

    def getTitle(self):
        time.sleep(3)
        return self.findElement(ProductPage.PAGE_TITLE)

    def assertTitle(self):
        self.assertWord(self.getTitle(), "Стационарный миксер Moulinex QuickMix HM3128B1")

    def addToCart(self):
        button = self.findElement(ProductPage.BUTTON_ADD_TO_CART)
        self.driver.execute_script("arguments[0].click();", button)
        print("Добавили миксер в корзину")


