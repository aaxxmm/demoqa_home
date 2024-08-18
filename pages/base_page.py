from selenium.webdriver.common.by import By
class BasePage:

    def __init__(self, driver):  # после self принимающиеся аргументы
        self.driver = driver
        self.base_url = 'https://www.saucedemo.com/'

    def visit(self):  # метод visit возвращает переход на страницу get
        return self.driver.get(self.base_url)

    def find_element(self, locator = 'div.login_logo'):  # метод find_element,аргумент locator
        return self.driver.find_element(By.CSS_SELECTOR, locator)

