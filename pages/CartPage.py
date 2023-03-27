from selenium.webdriver.common.by import By

from pages.AuthPage import AuthPage
from pages.BasePage import BasePage


class CartPage(BasePage):
    PAGE_TITLE = (By.XPATH, "//*[contains(text(), 'Корзина покупок')]")
    CONTACT_MAIL_FIELD = (By.XPATH, "//*[@placeholder = 'e-mail']")
    DELIVERY_STREET_FIELD = (By.XPATH, "//*[@id ='checkout__delivery_street']")
    DELIVERY_HOUSE_FIELD = (By.XPATH, "//*[@id ='checkout__delivery_house']")
    PAYMENT_TYPE_CASH = (By.XPATH, "//*[contains(text(), 'Наличными при получении')]")
    AGREEMENT_CHECKBOX = (By.XPATH, "//*[@class='basket-submit__confirm']")
    BUTTON_SUBMIT_BUY = (By.XPATH, "//button[contains(@class, 'basket-submit__buy')]")

    def getTitle(self):
        return self.findElement(CartPage.PAGE_TITLE)

    def assertTitle(self):
        self.assertWord(self.getTitle(), "Корзина покупок")

    def getContactEmail(self):
        return self.findElement(CartPage.CONTACT_MAIL_FIELD).get_attribute('value')

    def assertEmail(self):
        email = self.getContactEmail()
        login = AuthPage.EMAIL
        assert email == login

    def fillDelivery(self):
        self.findElement(CartPage.DELIVERY_STREET_FIELD).send_keys("Воронцовский б-р")
        self.findElement(CartPage.DELIVERY_HOUSE_FIELD).send_keys("32")
        print("Данные для доставки заполнены")

    def selectPaymentCash(self):
        return self.findElement(CartPage.PAYMENT_TYPE_CASH).click()

    def acceptAgreement(self):
        check_box = self.findElement(CartPage.AGREEMENT_CHECKBOX)
        self.driver.execute_script("arguments[0].click();", check_box)

    def checkClickable(self):
        self.findElement(CartPage.BUTTON_SUBMIT_BUY).is_displayed()
        print("Можно нажать на кнопку оформления заказа")









