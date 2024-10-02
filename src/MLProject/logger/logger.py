import logging
import os

# Define the directory where the logs will be stored
filedir = "logs"
# Create the directory if it doesn't exist
os.makedirs(filedir, exist_ok=True)

# Define the log file path
log_filepath = os.path.join(filedir, "running_log.log")

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]",
    handlers=[logging.FileHandler(filename=log_filepath)]
)

logging.info("This is a test")
