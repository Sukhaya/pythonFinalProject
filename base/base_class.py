import datetime


class Base():
    def __init__(self, driver):
        self.driver = driver


    """Method get current URL"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current URL " + get_url)


    """Method assert URL"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("URLs are equal")


    """Method assert word"""
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Equals")


    """Method screenshot"""
    def doScreenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%d.%m.%Y - %H.%M.%S")
        name_screenshot = 'screenshoot_' + now_date + '.png'
        self.driver.save_screenshot("/Users/mariasuhinina/PycharmProjects/pythonFinalProject/screen/" + name_screenshot)
