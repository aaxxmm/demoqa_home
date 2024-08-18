from pages.swag_labs import SwagLabs
def test_check_icon(browser): #browser-аргумент

    swag_labs_page = SwagLabs(browser) #
    swag_labs_page.visit() #посещаем страницу
    swag_labs_page.find_element()
    assert swag_labs_page.exist_icon()  #эл-т есть на странице