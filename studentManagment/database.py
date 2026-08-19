import logging 

from logging_config import setup_logging

logger = logging.getLogger(__name__)

def connect_to_db():
    try:
        raise ConnectionError("Unable to connect to database")
    except Exception as e:
        # print("Cannot connect to database:", e)
        logger.exception("DataBase Connection Failed")
