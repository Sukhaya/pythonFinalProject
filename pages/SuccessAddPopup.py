from pages.BasePage import BasePage

from selenium.webdriver.common.by import By


class SuccessAddPopup(BasePage):
    POPUP_TITLE = (By.XPATH, "//*[contains(text(), 'Товар успешно добавлен в корзину')]")
    BUTTON_GO_TO_CART = (By.XPATH, "//*[contains(text(), 'Перейти в корзину')]")

    def getTitle(self):
        return self.findElement(SuccessAddPopup.POPUP_TITLE)

    def assertTitle(self, word, result):
        self.assertWord(self.getTitle(), "Товар успешно добавлен в корзину")

    def goToCart(self):
        self.findElement(SuccessAddPopup.BUTTON_GO_TO_CART).click()
        print("Перешли в корзину")


