import logging
from pathlib import Path

LOG_PATH = Path(__file__).resolve().parent / "app.log"

logging.basicConfig(
    filename=LOG_PATH,
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_logger():
    return logging