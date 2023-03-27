

from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class StartPage(BasePage):
    LOGIN_ICON = (By.XPATH, "//*[contains(text(), 'Войти')]")

    def openAuthPage(self):
        icon = self.findElement(StartPage.LOGIN_ICON)
        icon.click()
        print("Открыли страницу для входа")





