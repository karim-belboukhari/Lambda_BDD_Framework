import logging
import os


def setup_logging(log_level=logging.INFO):
    # Define the exact log file path
    log_file = r".\logs\auto_log.log"

    # Ensure the logs directory exists
    log_dir = os.path.dirname(log_file)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Define the log format
    log_format = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(name)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Set up the root logger
    logger = logging.getLogger()
    logger.setLevel(log_level)

    # Console handler (for printing logs to the console)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(log_format)
    logger.addHandler(console_handler)

    # File handler (for writing logs to the specified file)
    file_handler = logging.FileHandler(log_file, mode='a')
    file_handler.setLevel(log_level)
    file_handler.setFormatter(log_format)
    logger.addHandler(file_handler)

    # Adding a debug message to confirm logging setup
    logger.info(f"Logging is set up. Log file: {log_file}")

    return logger
