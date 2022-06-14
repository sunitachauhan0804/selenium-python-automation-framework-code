import logging

from selenium.webdriver.common.by import By
from pages import admin_dashboard_page, change_password_page, my_accounts_page, edit_my_accounts_information_page, \
    admin_login_page
from base import web_driver_util
from utilities.custom_logger import custom_logger

log = custom_logger(loglevel=logging.WARNING)


def admin_form(driver):
    web_driver_util.set_text_to_element(driver, By.NAME, admin_login_page.admin_emailid_textfield,
                                        "admin1@gmail.com")
    web_driver_util.set_text_to_element(driver, By.NAME, admin_login_page.admin_password_textfield, "admin1")
    # get the value of verification code
    verification_no = web_driver_util.get_text_field_value(driver, By.NAME, admin_login_page.verification_no)
    web_driver_util.set_text_to_element(driver, By.NAME, admin_login_page.admin_verificate_code_textfield,
                                        verification_no)
    web_driver_util.click_element(driver, By.XPATH, admin_login_page.admin_login_button)
    log.warning(" Click admin login button then next page ADMIN DASHBOARD PAGE")
    # Clear button
    # web_driver_util.click_element(driver, By.XPATH, admin_login_page.admin_clear_button)
    manage_account(driver)


def manage_account(driver):
    log.warning(" manage_admin_login_account")
    web_driver_util.click_element(driver, By.XPATH, admin_dashboard_page.admin_menu)
    web_driver_util.click_element(driver, By.XPATH, admin_dashboard_page.admin_menu_my_account)
    web_driver_util.click_element(driver, By.XPATH, my_accounts_page.update_info_button)
    # Alert
    web_driver_util.alert_window(driver)
    log.warning("alert ok")
    update_account(driver)
    change_password(driver)


def update_account(driver):
    # Edit my account information
    web_driver_util.set_text_to_element(driver, By.NAME, edit_my_accounts_information_page.username_textfield, "akki")
    web_driver_util.set_text_to_element(driver, By.NAME, edit_my_accounts_information_page.email_id_textfield, "akki@gmail.com")
    web_driver_util.click_element(driver, By.XPATH, edit_my_accounts_information_page.update_product_button)
    log.warning("My Account Updated Successfully")


def change_password(driver):
    # Change password
    web_driver_util.click_element(driver, By.XPATH, admin_dashboard_page.admin_menu)
    web_driver_util.click_element(driver, By.XPATH, admin_dashboard_page.admin_menu_change_password)
    # admin_login_page.admin_password_textfield
    web_driver_util.set_text_to_element(driver, By.XPATH, change_password_page.current_password_text_field, 'admin1')
    web_driver_util.set_text_to_element(driver, By.NAME, change_password_page.new_password_text_field, 'admin1')
    web_driver_util.set_text_to_element(driver, By.NAME, change_password_page.confirm_passwors_text_field, 'admin1')
    web_driver_util.click_element(driver, By.XPATH, change_password_page.submit_button)
    # Alert for change password
    web_driver_util.alert_window(driver)
    log.warning("Password changed successfully")
