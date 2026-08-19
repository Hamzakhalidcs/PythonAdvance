import logging 
from logging_config import setup_logging

setup_logging()

logger = logging.getLogger(__name__)

students = {}

def add_student(student_id, name):
    if student_id in students:
        # print(f"Student with '{student_id}' already exists")
        logger.warning(f"Student With ID '{student_id}' already exists! Name :{students[student_id]}")

    else:
        students[student_id] = name
        # print(f"Student '{name}' added Successfully")
        logger.info(f"Student '{name}' With ID '{student_id}' added Successfully ")


add_student(1, "Hamza")
add_student(1, 'ASAD')
print(students)
    

success = add_student(2, "John")
if success:
    print("Student is added successfully.")

sucess = add_student(2, "Asad")
if not success:
    print("Student already exists!")
