import logging
import os
from datetime import datetime


# create logs directory if not exists
LOG_DIR =   os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_DIR, exist_ok=True)


#crate a log file with a timestamp

LOG_FILE_NAME = f"{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE_NAME)
 

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format='%(asctime)s - %(lineno)d - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
) 

# Expose the logger
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logging.info("Logging setup complete.")






# exception.py
# import sys
# from logger import logger

# def error_message_detail(error, error_detail: sys) -> str:
#     _, _, exc_tb = error_detail.exc_info()
#     file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown"
#     line_number = exc_tb.tb_lineno if exc_tb else -1
#     return f"Error occurred in script: [{file_name}] at line number: [{line_number}] with message: [{str(error)}]"

# class CustomException(Exception):
#     def __init__(self, error_message: Exception, error_detail: sys):
#         self.error_message = error_message_detail(error_message, error_detail)
#         super().__init__(self.error_message)
#         logger.error(self.error_message)

#     def __str__(self):
#         return self.error_message
