# app/logging_config.py
import logging
from logging.handlers import RotatingFileHandler
import os

LOG_DIR = "logs"
LOG_FILE = "app.log"

os.makedirs(LOG_DIR, exist_ok=True)

def setup_logging():
    log_path = os.path.join(LOG_DIR, LOG_FILE)

    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[
            RotatingFileHandler(log_path, maxBytes=5_000_000, backupCount=5)
        ]
    )
