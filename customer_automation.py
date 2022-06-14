
# Home ,Product , Order, Customer, Admin
from selenium.webdriver.common.by import By
from pages import admin_dashboard_page
from base import web_driver_util


def click_customer_menu(driver):
    web_driver_util.click_element(driver, By.XPATH, admin_dashboard_page.admin_customer_menu)  # customer
    web_driver_util.click_element(driver, By.XPATH, admin_dashboard_page.admin_customer_menu_view_contact)
    web_driver_util.click_element(driver, By.XPATH, admin_dashboard_page.admin_customer_menu)  # customer
    web_driver_util.click_element(driver, By.XPATH, admin_dashboard_page.admin_customer_menu_view_customer)

