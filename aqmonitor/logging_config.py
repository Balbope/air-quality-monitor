# Жүйенің жұмыс барысында орын алатын оқиғаларды журналға (логқа) жазу жүйесі.


import logging
from logging.handlers import RotatingFileHandler
import os

# Лог файлы сақталатын бума
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Лог файлының атауы
log_file = os.path.join(LOG_DIR, "aqmonitor.log")

# Негізгі логгер
logger = logging.getLogger("aqmonitor")
logger.setLevel(logging.INFO)

# Лог файлын айналдырып сақтау (көлем асып кетпеу үшін)
file_handler = RotatingFileHandler(log_file, maxBytes=1_000_000, backupCount=3)

# Лог жазу форматы
formatter = logging.Formatter(
    "%(asctime)s [%(levelname)s] %(name)s - %(message)s"
)
file_handler.setFormatter(formatter)

# Егер бұрын қосылмаған болса, хэндлерді қосамыз
if not logger.handlers:
    logger.addHandler(file_handler)
