import logging 
from logging.handlers import RotatingFileHandler
from pathlib import Path

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = RotatingFileHandler(
    "rotation.log",
    maxBytes=200, 
    backupCount=3
)

formatter = logging.Formatter(
    "%(asctime)s, %(levelname)s, %(name)s,  %(message)s"
)

handler.setFormatter(formatter)
logger.addHandler(handler)

for i in range(50):
    logger.info(f"This is test log message number {i}")

path = Path("rotation.log.1")
size = path.stat().st_size
print(size)