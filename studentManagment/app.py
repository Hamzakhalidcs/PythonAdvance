import logging 

from logging_config import setup_logging

setup_logging()

import student
import database

logger = logging.getLogger(__name__)

logger.info("Application Started")

student.add_student(1, "Hamza")
student.add_student(1, 'ASAD')

database.connect_to_db()

logger.info("Application Finished")
