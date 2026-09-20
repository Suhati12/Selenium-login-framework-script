import pytest
from pages.login_page import LoginPage

# TC_01: Positive Login Test
def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("student", "Password123")
    assert "Logged In Successfully" in login_page.get_success_heading()


# TC_02 - TC_04: Equivalence Partitioning & Boundary Testing
@pytest.mark.parametrize("username, password, expected_error", [
    ("invalidUser", "Password123", "Your username is invalid!"),
    ("student", "wrongPassword", "Your password is invalid!"),
    ("", "", "Your username is invalid!")
])
def test_invalid_logins(driver, username, password, expected_error):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)
    assert expected_error in login_page.get_error_message()


# TC_05: UI Validation Test
def test_ui_validation(driver):
    login_page = LoginPage(driver)
    login_page.open()
    assert driver.find_element(*login_page.username_input).is_displayed()
    assert driver.find_element(*login_page.password_input).is_displayed()
    assert driver.find_element(*login_page.submit_button).is_displayed()