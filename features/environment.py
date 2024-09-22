from utilities.driver_manager import get_driver, close_driver
import logging


def before_all(context):
    # Initialize logging and any global setup
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting test suite")


def before_scenario(context, scenario):
    # Open a new browser window for each scenario
    logging.info(f"Starting scenario: {scenario.name}")
    browser = context.config.userdata.get("browser", "edge")
    context.driver = get_driver(browser)


def after_scenario(context, scenario):
    # Close the browser window after each scenario
    logging.info(f"Finished scenario: {scenario.name}")
    if context.driver:
        close_driver(context.driver)


def after_all(context):
    logging.info("Test suite finished")
