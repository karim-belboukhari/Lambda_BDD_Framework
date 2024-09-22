from utilities.driver_manager import get_driver, close_driver
from utilities.logging_setup import setup_logging


def before_all(context):
    # Initialize logging and any global setup
    logger = setup_logging()
    logger.info("Starting the test suite.")


def before_scenario(context, scenario):
    # Open a new browser window for each scenario
    logger = setup_logging()
    logger.info(f"Starting scenario: {scenario.name}")
    browser = context.config.userdata.get("browser", "edge")
    context.driver = get_driver(browser)


def after_scenario(context, scenario):
    # Close the browser window after each scenario
    logger = setup_logging()
    logger.info(f"Finished scenario: {scenario.name}")
    if context.driver:
        close_driver(context.driver)


def after_all(context):
    logger = setup_logging()
    logger.info("Test suite finished")
