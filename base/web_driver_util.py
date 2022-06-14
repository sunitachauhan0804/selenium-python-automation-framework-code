from selenium import webdriver
from selenium.webdriver.support.select import Select


def get_driver():
    return webdriver.Chrome(executable_path="D:\data\sk\softwares\chromedriver.exe")


def launch_browser(driver):
    driver.get("http://localhost:8080/oss/index.jsp")


def maximize_window(driver):
    driver.maximize_window()


def click_element(driver, by_ref, element_ref):
    element = driver.find_element(by_ref, element_ref)
    element.click()


def set_text_to_element(driver, by_ref, element_ref, element_value):
    element = driver.find_element(by_ref, element_ref)
    element.clear()
    element.send_keys(element_value)


def set_drop_down(driver, by_ref, element_ref, element_value):
    element = driver.find_element(by_ref, element_ref)
    drop_down = Select(element)
    drop_down.select_by_visible_text(element_value)
    print("Drop down")
    # drop_down.select_by_index(1)


def scroll_down_page(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


def alert_window(driver):
    driver.switch_to.alert.accept()


# get text field value
def get_text_field_value(driver, by_ref, element_ref):
    element = driver.find_element(by_ref, element_ref).get_attribute("value")
    return element


# read label
def get_label_value(driver, by_ref, element_ref):
    element = driver.find_element(by_ref, element_ref).text
    return element
