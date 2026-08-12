# """
# activation and installation and checking installation
# source .venv/bin/activate 
#  which pip 
#  pip list 
#  pip install requests
#  pip list string for VirtualEnvironmentPractice.app
#  pip freeze > requirements.txt
# """

# import logging

# # logging.basicConfig(level=logging.INFO)

# # logging.debug("Debugging application")
# # logging.info("Application Started")
# # logging.warning("Low disk space")
# # logging.error("Could not connect to database")
# # logging.critical("Application crashed")


# logger = logging.getLogger(__name__)

# logging.basicConfig(
#     filename= "app.log",
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
# )

# logger.info("Applicaiton Started")
# logger.warning("Student Already Exists")
# logger.error("Unable to save student Data")

# import database

import logging

logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("app.log")
stream_handler = logging.StreamHandler()

file_formatter = logging.Formatter(
    "%(asctime)s, %(levelname)s, %(name)s, %(message)s"
)

stream_formatter = logging.Formatter(
    "%(levelname)s,  %(message)s"
)

file_handler.setLevel(logging.INFO)
stream_handler.setLevel(logging.WARNING)

file_handler.setFormatter(file_formatter)
stream_handler.setFormatter(stream_formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

logger.debug("Debugging application")
logger.info("Application Started")
logger.warning("Student Already Exists")
logger.error("Unable to save Student")
logger.critical("Application Crashed")

