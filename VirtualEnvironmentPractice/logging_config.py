import logging 

def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    if logger.handlers:
        return 
    

    handler = logging.FileHandler("app.log")

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

    handler.setFormatter(formatter)
    logger.addHandler(handler)
    