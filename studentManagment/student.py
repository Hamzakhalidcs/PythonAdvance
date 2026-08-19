import logging 

from logging_config import setup_logging

logger = logging.getLogger(__name__)

students = {}

def add_student(student_id, name):

    if student_id in students:
        logger.warning(
            f"Student With ID '{student_id}' already exists! Name :{students[student_id]}"
            )

    else:
        students[student_id] = name

        logger.info(
            f"Student '{name}' With ID '{student_id}' added Successfully "
            )



    
