import datetime

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://shop.moulinex.ru/"
        self.driver.maximize_window()

    def findElement(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator),
                                                      message=f"Can't find element by locator {locator}")

    def findElements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def openUrl(self):
        return self.driver.get(self.base_url)

    def doScreenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%d.%m.%Y - %H.%M.%S")
        name_screenshot = 'screenshoot_' + now_date + '.png'
        self.driver.save_screenshot("/Users/mariasuhinina/PycharmProjects/pythonFinalProject/screen/" + name_screenshot)

    def assertWord(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Заголовок совпадает с ожидаемым")

    def assertUrl(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Находимся на верной странице")

    def getCurrentUrl(self):
        return self.driver.current_url


