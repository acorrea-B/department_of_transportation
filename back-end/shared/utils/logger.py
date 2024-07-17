import logging
from shared.config.env_vars import Config


def setup_logging():
    log_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    console_handler.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    console_handler.setLevel(logging.INFO)

    app_logger = logging.getLogger("root")
    app_logger.setLevel(logging.INFO)

    return app_logger


def logger_error(message):
    logger = setup_logging()
    logger.error(message)


def logger_info(message):
    logger = setup_logging()
    logger.info(message)
