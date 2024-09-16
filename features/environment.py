from utilities.driver_manager import get_driver, close_driver
import logging


def before_all(context):
    # Initialize logging and any global setup
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting test suite")
    context.driver = get_driver()


def before_scenario(context, scenario):
    logging.info(f"Starting scenario: {scenario.name}")
    context.driver = get_driver()


def after_scenario(context, scenario):
    if scenario.status == "failed":
        context.driver.save_screenshot(f'screenshots/{scenario.name}.png')
    logging.info(f"Ending scenario: {scenario.name}")
    close_driver(context.driver)


def after_all(context):
    logging.info("Test suite finished")
    close_driver(context.driver)
