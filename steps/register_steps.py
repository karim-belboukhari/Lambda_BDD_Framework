from behave import *
from utilities.driver_manager import get_driver, close_driver
from utilities.read_config import get_config_values
from selenium.webdriver.common.by import By
import random
import string


@given("the user launches the site")
def step_launch_the_site(context):
    context.driver = get_driver()
    context.driver.get(get_config_values("url", "login_url"))


@when("the user selects the register option")
def step_select_register(context):
    context.driver.find_element(By.XPATH, "//aside[@id='column-right']//descendant::a[text()=' Register']").click()


@when("the user fills in the registration fields")
def step_fill_registration_fields_with_valid_inputs(context):
    context.driver.find_element(By.ID, "input-firstname").send_keys("karim")
    context.driver.find_element(By.ID, "input-lastname").send_keys("Belboukhari")
    context.driver.find_element(By.ID, "input-email").send_keys(f"{random_generator()}@yopmail.com")
    context.driver.find_element(By.ID, "input-telephone").send_keys(f"{random_numbers()}")
    context.driver.find_element(By.ID, "input-password").send_keys("Test@12345$")
    context.driver.find_element(By.ID, "input-confirm").send_keys("Test@12345$")
    context.driver.find_element(By.XPATH, "//*[@class='custom-control-label' and @for='input-agree']").click()
    context.driver.find_element(By.XPATH, "//div[@class='float-right']//descendant::input[@type='submit']").click()


@then("the user register successfully")
def step_check_registration(context):
    title = context.driver.title
    if title == "Your Account Has Been Created!":
        assert True
    else:
        context.driver.save_screenshots(r".\Screenshots" + "fail_registration.png")
        assert False


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


def random_numbers(size=10, chars=string.digits):
    return ''.join(random.choice(chars) for x in range(size))


