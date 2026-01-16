import allure
from pages.login_page import LoginPage


@allure.feature("Login")
class TestLogin:

    @allure.story("Successful login")
    def test_successful_login(self, driver):
        page = LoginPage(driver)
        page.open()
        page.login("standard_user", "secret_sauce")

        assert page.is_inventory_page_opened()
        assert "inventory.html" in driver.current_url

    @allure.story("Login with wrong password")
    def test_login_wrong_password(self, driver):
        page = LoginPage(driver)
        page.open()
        page.login("standard_user", "wrong_password")

        assert "Epic sadface" in page.get_error_message()

    @allure.story("Locked out user login")
    def test_locked_out_user(self, driver):
        page = LoginPage(driver)
        page.open()
        page.login("locked_out_user", "secret_sauce")

        assert "locked out" in page.get_error_message().lower()

    @allure.story("Login with empty fields")
    def test_login_empty_fields(self, driver):
        page = LoginPage(driver)
        page.open()
        page.login()

        assert "Username is required" in page.get_error_message()

    @allure.story("Performance glitch user login")
    def test_performance_glitch_user(self, driver):
        page = LoginPage(driver)
        page.open()
        page.login("performance_glitch_user", "secret_sauce")

        assert page.is_inventory_page_opened()
        assert "inventory.html" in driver.current_url