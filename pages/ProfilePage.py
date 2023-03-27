from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class ProfilePage(BasePage):
    PAGE_TITLE = (By.XPATH, "//*[@class = 'page-content__header']")
    MENU_BUTTON = (By.XPATH, "//span[contains(text(), 'Каталог')]")
    MIXERS = (By.XPATH, "//*[contains(text(), 'Миксеры')]")

    def getTitle(self):
        return self.findElement(ProfilePage.PAGE_TITLE)

    def assertTitle(self):
        self.assertWord(self.getTitle(), "Личная информация")

    def openMenu(self):
        self.findElement(ProfilePage.MENU_BUTTON).click()
        print("Открыли меню сайта")

    def chooseMixers(self):
        self.findElement(ProfilePage.MIXERS).click()
        print("Выбрали миксеры")


