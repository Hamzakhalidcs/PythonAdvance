"""
activation and installation and checking installation
source .venv/bin/activate 
 which pip 
 pip list 
 pip install requests
 pip list string for VirtualEnvironmentPractice.app
 pip freeze > requirements.txt
"""

import logging

# logging.basicConfig(level=logging.INFO)

# logging.debug("Debugging application")
# logging.info("Application Started")
# logging.warning("Low disk space")
# logging.error("Could not connect to database")
# logging.critical("Application crashed")


logger = logging.getLogger(__name__)

logging.basicConfig(
    filename= "app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

logger.info("Applicaiton Started")
logger.warning("Student Already Exists")
logger.error("Unable to save student Data")
