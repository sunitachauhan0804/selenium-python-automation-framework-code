import pytest
from base import web_driver_util


@pytest.fixture(scope="class")
def setup(request):
    driver = web_driver_util.get_driver()
    web_driver_util.launch_browser(driver)
    web_driver_util.maximize_window(driver)
    request.cls.driver = driver
    yield
    driver.close()
