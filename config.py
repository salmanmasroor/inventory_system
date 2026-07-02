from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DB_PATH = BASE_DIR / "inventory.db"
LOG_PATH = BASE_DIR / "app.log"

LOW_STOCK_THRESHOLD = 5
SCHEDULER_INTERVAL_SECONDS = 50
