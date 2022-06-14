# Home ,Product , Order, Customer, Admin
import logging
from selenium.webdriver.common.by import By
from pages import add_product_page, admin_dashboard_page, view_product_page
from base import web_driver_util
from utilities.custom_logger import custom_logger

log = custom_logger(loglevel=logging.WARNING)


def manage_home(driver):
    web_driver_util.click_element(driver, By.XPATH, admin_dashboard_page.admin_home_button)  # Home
    log.warning("Click on home_menu")


def click_product_menu(driver):
    web_driver_util.click_element(driver, By.ID, admin_dashboard_page.admin_product_menu)    # product
    log.warning("Click on product_menu")
    view_product(driver)
    add_product(driver)


def view_product(driver):
    web_driver_util.click_element(driver, By.XPATH, admin_dashboard_page.admin_product_menu_view_product)
    log.warning("Click on view_products")
    web_driver_util.click_element(driver, By.XPATH, view_product_page.edit_product_button)
    log.warning("Click on edit button")
    web_driver_util.scroll_down_page(driver)
    web_driver_util.set_drop_down(driver, By.NAME, view_product_page.product_status_drop_down, 'In-Active')
    web_driver_util.click_element(driver, By.XPATH, view_product_page.product_update_button)
    log.warning("Update product done")


def add_product(driver):
    web_driver_util.click_element(driver, By.ID, admin_dashboard_page.admin_product_menu)
    log.warning("Click again product")
    web_driver_util.click_element(driver, By.XPATH, admin_dashboard_page.admin_product_menu_add_product)
    log.warning("add product")
    web_driver_util.set_text_to_element(driver, By.NAME, add_product_page.product_name_text_field, "Women Dress")
    web_driver_util.set_text_to_element(driver, By.NAME, add_product_page.product_price_text_field, 500)
    web_driver_util.set_text_to_element(driver, By.XPATH, add_product_page.product_description_text_field,
                                        "Nice Dress for Party Wear")
    web_driver_util.set_text_to_element(driver, By.NAME, add_product_page.product_mrp_price_text_field, 800)
    # scroll down the page
    web_driver_util.scroll_down_page(driver)
    web_driver_util.set_drop_down(driver, By.NAME, add_product_page.Product_status_drop_down, "Active")
    web_driver_util.set_drop_down(driver, By.NAME, add_product_page.product_category_drop_down, "Mens/Womens Wear")
    web_driver_util.click_element(driver, By.XPATH, add_product_page.add_product_button)
    web_driver_util.alert_window(driver)
    log.warning("Product added")
    # web_driver_util.click_element(driver, By.XPATH, add_product_page.reset_button)


