# Home ,Product , Order,customer , Admin
import logging
from selenium.webdriver.common.by import By
from pages import admin_dashboard_page
from base import web_driver_util
from utilities.custom_logger import custom_logger

log = custom_logger(loglevel=logging.DEBUG)


def click_order_menu(driver):
    log.debug(" enter in fun order button ")
    web_driver_util.click_element(driver, By.XPATH, admin_dashboard_page.admin_order_menu)
    log.debug("Click order button ")
    view_all_order(driver)
    view_pending_order(driver)
    view_delivered_order(driver)


def view_all_order(driver):
    web_driver_util.click_element(driver, By.XPATH, admin_dashboard_page.admin_order_menu_view_all_order)
    log.info(" All order ")


def view_pending_order(driver):
    web_driver_util.click_element(driver, By.XPATH, admin_dashboard_page.admin_order_menu)      # click again order
    web_driver_util.click_element(driver, By.XPATH, admin_dashboard_page.admin_order_menu_view_pending_order)
    log.info("All pending order")


def view_delivered_order(driver):
    web_driver_util.click_element(driver, By.XPATH, admin_dashboard_page.admin_order_menu)      # click again order
    web_driver_util.click_element(driver, By.XPATH, admin_dashboard_page.admin_order_menu_view_delivered_order)
    log.info("All delivered order")
