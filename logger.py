import logging

from config import LOG_PATH

logging.basicConfig(
    filename=LOG_PATH,
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def get_logger():
    return logging
