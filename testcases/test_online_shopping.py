import pytest

import admin_automation
import customer_automation
import order_automation
import product_automation
import smart_shop_automation


# Launch the browser

@pytest.mark.usefixtures("setup")
class TestOnlineShopping:

    def test_admin_login_link(self):
        # Smart shop page admin login link
        admin_login_text = smart_shop_automation.click_admin_login_link(self.driver)
        assert admin_login_text == "ADMIN LOGIN"

    # Admin login form
    def test_admin_login_form(self):
        admin_automation.admin_form(self.driver)

    #def test_product(self):
     #   product_automation.click_product_menu(self.driver)

    def test_order(self):
        order_automation.click_order_menu(self.driver)

    #def test_customer(self):
     #   customer_automation.click_customer_menu(self.driver)




        # Log me out
        #web_driver_util.click_element(driver, By.XPATH, my_accounts_page.log_me_out_button)
        #web_driver_util.click_element(driver, By.XPATH, admin_login_page.home_link)
        print("done")

