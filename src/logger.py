import logging    
import os
from datetime import datetime


LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # Create a log file with the current date and time
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE) # Create a path to the log file
os.makedirs(logs_path, exist_ok=True) # Create the logs directory if it doesn't exist

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE) # Create a path to the log file

logging.basicConfig(
    filename = LOG_FILE_PATH, # Set the log file path
    format= "[%(asctime)s] %(lineno)d %(levelname)s: %(message)s", # Set the log format
    level=logging.INFO # Set the log level to INFO
)


if __name__ == "__main__":
    logging.info("Logging has started") # Log a test message
