# Create a setup_logging() function that:

# Uses the root logger or a suitable central logger.
# Sets the logging level to INFO.
# Uses a RotatingFileHandler.
# Saves logs inside logs/app.log.
# Maximum size: 5 KB
# Keeps 3 backup files.
# Also sends logs to the terminal using StreamHandler.
# File and terminal logs should have appropriate formatting.
# Prevents duplicate handlers if setup_logging() is called twice.

import logging 
from logging.handlers import RotatingFileHandler

def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    stream_handler = logging.StreamHandler()

    if logger.handlers:
        return
    

    rotating_file_handler = RotatingFileHandler(
        "logs/app.log" ,
        maxBytes=5120, 
        backupCount=3
    )

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

    stream_formatter = logging.Formatter(
        "%(levelname)s, %(message)s"
    )

    stream_handler.setLevel(logging.WARNING)
    stream_handler.setFormatter(stream_formatter)


    rotating_file_handler.setFormatter(formatter)

    
    logger.addHandler(rotating_file_handler)
    logger.addHandler(stream_handler)