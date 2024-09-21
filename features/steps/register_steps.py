from behave import *
from utilities.read_config import get_config_values
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchFrameException
import random
import string
import os


@given("the user launches the site")
def step_launch_the_site(context):
    try:
        context.driver.get(get_config_values("url", "login_url"))
    except Exception as e:
        context.driver.save_screenshot(os.path.join(r".\Screenshots", "launch_fail.png"))
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
        context.driver.find_element(By.ID, "input-firstname").send_keys("karim")
        context.driver.find_element(By.ID, "input-lastname").send_keys("Belboukhari")
        context.driver.find_element(By.ID, "input-email").send_keys(f"{random_generator()}@yopmail.com")
        context.driver.find_element(By.ID, "input-telephone").send_keys(f"{random_numbers()}")
        context.driver.find_element(By.ID, "input-password").send_keys("Test@12345$")
        context.driver.find_element(By.ID, "input-confirm").send_keys("Test@12345$")
        context.driver.find_element(By.XPATH, "//*[@class='custom-control-label' and @for='input-agree']").click()
        context.driver.find_element(By.XPATH, "//div[@class='float-right']//descendant::input[@type='submit']").click()
    except Exception as e:
        context.driver.save_screenshot(r".\Screenshots", "Registration_steps_fail.png")
        raise AssertionError(f"Fail to complete the registration steps {e}")


@then("the user register successfully")
def step_check_registration(context):
    title = context.driver.title
    if title == "Your Account Has Been Created!":
        assert True
    else:
        context.driver.save_screenshot(os.path.join(r".\Screenshots", "fail_registration.png"))
        raise AssertionError(f"Registration failed. Page title is '{title}'")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def random_numbers(size=10, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
