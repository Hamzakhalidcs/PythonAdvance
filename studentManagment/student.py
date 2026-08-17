import logging 
from logging_config import setup_logging

setup_logging()

logger = logging.getLogger(__name__)

students = {}

def add_student(student_id, name):
    if student_id in students:
        print(f"Student with '{student_id}' already exists")
    else:
        students[student_id] = name
    

