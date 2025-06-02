'''import os
import logging
import sys

logging_str="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"


log_dir="logs"
log_filepath=os.path.join(log_dir , "logging.log")
os.makedirs(log_dir , exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger=logging.getLogger("datasciencelogger")
'''
import os
import logging
import sys

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir, "logging.log")
os.makedirs(log_dir, exist_ok=True)

# Create logger
logger = logging.getLogger("datasciencelogger")
logger.setLevel(logging.INFO)
logger.propagate = False  # Avoid double logging if root logger is configured

# Add handlers ONLY if they aren't already added
if not logger.hasHandlers():
    file_handler = logging.FileHandler(log_filepath)
    stream_handler = logging.StreamHandler(sys.stdout)

    formatter = logging.Formatter(logging_str)
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

logger.info("Logger initialized successfully in datascience package.")


