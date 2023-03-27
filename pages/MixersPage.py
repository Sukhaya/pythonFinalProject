
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.BasePage import BasePage


class MixersPage(BasePage):
    SERIA_FILTER = (By.XPATH, "//*[contains(text(), 'Серия')]")
    PRICE_FILTER = (By.XPATH, "//*[contains(text(), 'Цена')]")
    QUICK_CHECK_BOX = (By.XPATH, "//span[contains(text(), 'QuickMix')]")
    MIN_PRICE_FIELD = (By.XPATH, "//*[@id='__next']/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/input")
    MAX_PRICE_FIELD = (By.XPATH, "//*[@id='__next']/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[2]/div/div/div/div/div/div[2]/div/input")
    MIXER = (By.XPATH, "//*[contains(text(), 'Стационарный миксер Moulinex QuickMix HM3128B1')]")



    def assertCurrentUrl(self):
        self.assertUrl('https://shop.moulinex.ru/category/podgotovka/miksery')

    def openSeriaFilter(self):
        return self.findElement(MixersPage.SERIA_FILTER).click()

    def openPriceFilter(self):
        return self.findElement(MixersPage.PRICE_FILTER).click()

    def clickCheckBoxSeria(self):
        return self.findElement(MixersPage.QUICK_CHECK_BOX).click()

    def setMinPrice(self):
        self.findElement(MixersPage.MIN_PRICE_FIELD).send_keys(Keys.BACKSPACE*4)
        self.findElement(MixersPage.MIN_PRICE_FIELD).send_keys("900")
        print("Установили фильтр минимальной цены")

    def setMaxPrice(self):
        self.findElement(MixersPage.MAX_PRICE_FIELD).send_keys(Keys.BACKSPACE*4)
        self.findElement(MixersPage.MAX_PRICE_FIELD).send_keys("000")
        print("Установили фильтр максимальной цены")

    def selectMixer(self):
        self.findElement(MixersPage.MIXER).click()
        print("Выбрали нужный миксер по итогам фильтров")






