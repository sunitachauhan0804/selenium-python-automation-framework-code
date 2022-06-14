# Home ,Product , Order,customer , Admin
from selenium.webdriver.common.by import By
from pages import admin_dashboard_page
from base import web_driver_util


def click_order_menu(driver):
    web_driver_util.click_element(driver, By.XPATH, admin_dashboard_page.admin_order_menu)      # order
    print("order")
    view_all_order(driver)
    view_pending_order(driver)
    view_delivered_order(driver)


def view_all_order(driver):
    web_driver_util.click_element(driver, By.XPATH, admin_dashboard_page.admin_order_menu_view_all_order)
    print("all order")


def view_pending_order(driver):
    web_driver_util.click_element(driver, By.XPATH, admin_dashboard_page.admin_order_menu)      # click again order
    web_driver_util.click_element(driver, By.XPATH, admin_dashboard_page.admin_order_menu_view_pending_order)
    print("all pending order")


def view_delivered_order(driver):
    web_driver_util.click_element(driver, By.XPATH, admin_dashboard_page.admin_order_menu)      # click again order
    web_driver_util.click_element(driver, By.XPATH, admin_dashboard_page.admin_order_menu_view_delivered_order)
    print("all delivered order")
