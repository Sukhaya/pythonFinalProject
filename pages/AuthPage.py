from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class AuthPage(BasePage):
    EMAIL = "sukhoi.test@gmail.com"
    PASSWORD = "sukhoi.tes"

    EMAIL_FIELD = (By.XPATH, "//*[@id='mail']")
    PASSWORD_FIELD = (By.XPATH, "//*[@id='password_login']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    ACCEPT_COOKIES = (By.XPATH, "//*[@id='footer-react']/div/div[5]/div[2]/button/span")


    def assertCurrentUrl(self):
        self.assertUrl('https://shop.moulinex.ru/login')

    def fillEmail(self):
        return self.findElement(AuthPage.EMAIL_FIELD).send_keys(AuthPage.EMAIL)

    def fillPassword(self):
        return self.findElement(AuthPage.PASSWORD_FIELD).send_keys(AuthPage.PASSWORD)

    def clickLogin(self):
        self.findElement(AuthPage.ACCEPT_COOKIES).click()
        return self.findElement(AuthPage.LOGIN_BUTTON).click()
