import logging

from selenium.webdriver.common.by import By
from pages import smart_shop_page, admin_login_page
from base import web_driver_util
from utilities.custom_logger import custom_logger

log = custom_logger(loglevel=logging.DEBUG)


def click_admin_login_link(driver):
    web_driver_util.click_element(driver, By.XPATH, smart_shop_page.admin_login_link)
    log.debug("Click on login link")
    admin_login_text = web_driver_util.get_label_value(driver, By.XPATH, admin_login_page.admin_login_label)
    log.info("Admin login form")
    return admin_login_text
