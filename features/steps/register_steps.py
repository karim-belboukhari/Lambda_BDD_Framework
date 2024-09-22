from behave import *
from utilities.read_config import get_config_values
from selenium.common.exceptions import NoSuchFrameException
from selenium.webdriver.common.by import By
import pyautogui
import random
import string
import allure
import os


@given("the user launches the site")
def step_launch_the_site(context):
    try:
        context.driver.get(get_config_values("url", "login_url"))
        context.driver.maximize_window()
        context.driver.implicitly_wait(10)
    except Exception as e:
        capture_full_desktop_screenshot("launch_fail.png")
        raise AssertionError(f"failed to launch the site{e}")


@when("the user selects the register option")
def step_select_register(context):
    try:
        context.driver.find_element(By.XPATH, "//aside[@id='column-right']//descendant::a[text()=' Register']").click()
    except NoSuchFrameException as e:
        raise AssertionError(f"Fail to click on Register{e}")


@when("the user fills in the registration fields")
def step_fill_registration_fields_with_valid_inputs(context):
    try:
        # storing my Variables
        context.first_name = "karim"
        context.last_name = "Bel Boukhari"
        context.email = f"{random_generator()}@yopmail.com"
        context.number = f"{random_numbers()}"
        context.password = "Test@12345$"
        context.confirm_password = "Test@12345$"

        # locating my registration elements
        context.driver.find_element(By.ID, "input-firstname").send_keys(context.first_name)
        context.driver.find_element(By.ID, "input-lastname").send_keys(context.last_name)
        context.driver.find_element(By.ID, "input-email").send_keys(context.email)
        context.driver.find_element(By.ID, "input-telephone").send_keys(context.number)
        context.driver.find_element(By.ID, "input-password").send_keys(context.password)
        context.driver.find_element(By.ID, "input-confirm").send_keys(context.confirm_password)
        context.driver.find_element(By.XPATH, "//*[@class='custom-control-label' and @for='input-agree']").click()
        context.driver.find_element(By.XPATH, "//div[@class='float-right']//descendant::input[@type='submit']").click()
    except Exception as e:
        capture_full_desktop_screenshot("Registration_steps_fail.png")
        raise AssertionError(f"Fail to complete the registration steps {e}")


@when("the user leaves The required fields empty")
def step_all_fields_empty(context):

    try:
        # storing my Variables
        context.first_name = ""
        context.last_name = ""
        context.email = f""
        context.number = f""
        context.password = ""
        context.confirm_password = ""

        # locating my registration elements
        context.driver.find_element(By.ID, "input-firstname").send_keys(context.first_name)
        context.driver.find_element(By.ID, "input-lastname").send_keys(context.last_name)
        context.driver.find_element(By.ID, "input-email").send_keys(context.email)
        context.driver.find_element(By.ID, "input-telephone").send_keys(context.number)
        context.driver.find_element(By.ID, "input-password").send_keys(context.password)
        context.driver.find_element(By.ID, "input-confirm").send_keys(context.confirm_password)
        context.driver.find_element(By.XPATH, "//*[@class='custom-control-label' and @for='input-agree']").click()
        context.driver.find_element(By.XPATH, "//div[@class='float-right']//descendant::input[@type='submit']").click()


    except Exception as e:
        capture_full_desktop_screenshot("Registration_steps_fail.png")
        raise AssertionError(f"Fail to complete the registration steps {e}")


@then("the user register successfully")
def step_check_registration(context):
    title = context.driver.title
    if title == "Your Account Has Been Created!":
        assert True
    else:
        capture_full_desktop_screenshot("fail_registration.png")
        raise AssertionError(f"Registration failed. Page title is '{title}'")


@then("the user sees an error message for missing required fields")
def step_assert_error_messages(context):
    try:
        # Assertions for First Name error message
        first_name_error = context.driver.find_element(By.XPATH,
                                                       "//input[@id='input-firstname']/following-sibling::div[@class='text-danger']")
        assert first_name_error.is_displayed(), "First Name error message is not displayed"
        assert "vvvFirst Name must be between 1 and 32 characters!" in first_name_error.text,\
            f"Expected error: 'First Name must be between 1 and 32 characters!', but got: {first_name_error.text}"

        # Assertions for Last Name error message
        last_name_error = context.driver.find_element(By.XPATH,
                                                      "//input[@id='input-lastname']/following-sibling::div[@class='text-danger']")
        assert last_name_error.is_displayed(), "Last Name error message is not displayed"
        assert "Last Name must be between 1 and 32 characters!" in last_name_error.text, \
            f"Expected error: 'Last Name must be between 1 and 32 characters!', but got: {last_name_error.text}"

        # Assertions for Email error message
        email_error = context.driver.find_element(By.XPATH,
                                                  "//input[@id='input-email']/following-sibling::div[@class='text-danger']")
        assert email_error.is_displayed(), "Email error message is not displayed"
        assert "E-Mail Address does not appear to be valid!" in email_error.text, \
            f"Expected error: 'E-Mail Address does not appear to be valid!', but got: {email_error.text}"

        # Assertions for Telephone error message
        telephone_error = context.driver.find_element(By.XPATH,
                                                      "//input[@id='input-telephone']/following-sibling::div[@class='text-danger']")
        assert telephone_error.is_displayed(), "Telephone error message is not displayed"
        assert "Telephone must be between 3 and 32 characters!" in telephone_error.text, \
            f"Expected error: 'Telephone must be between 3 and 32 characters!', but got: {telephone_error.text}"

        # Assertions for Password error message
        password_error = context.driver.find_element(By.XPATH,
                                                     "//input[@id='input-password']/following-sibling::div[@class='text-danger']")
        assert password_error.is_displayed(), "Password error message is not displayed"
        assert "Password must be between 4 and 20 characters!" in password_error.text, \
            f"Expected error: 'Password must be between 4 and 20 characters!', but got: {password_error.text}"


    except Exception as e:
        capture_full_desktop_screenshot("error_messages_fails")
        raise AssertionError(f"Failed to assert error messages: {e}")







def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def random_numbers(size=10, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


# setup of my full desktop screenshot using pyautoGui
def capture_full_desktop_screenshot(filename):
    screenshot = pyautogui.screenshot()
    screenshots_dir = r".\Screenshots"
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)
    filepath = os.path.join(screenshots_dir, f"{filename}.png")
    screenshot.save(filepath)
    # Attach to Allure
    allure.attach.file(filepath, name=filename, attachment_type=allure.attachment_type.PNG)

