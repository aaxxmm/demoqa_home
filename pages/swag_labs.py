from selenium.common import NoSuchElementException

from pages.base_page import BasePage  #наследуем от BasePage

class SwagLabs(BasePage):
    def exist_icon(self):
        try:    #конструкция
            self.find_element(locator = 'div.login_logo')
        except NoSuchElementException:   #исключение
            return False
        return True
