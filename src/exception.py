import sys
from logger import logger

def error_message_detail(error, error_detail: sys):
    """
    Generates a detailed error message.

    Args:
        error (Exception): The exception instance.
        error_detail (sys): The sys module to access the exc_info.

    Returns:
        str: A formatted string containing the error type, value, and traceback.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    return f"Error occurred in script: [{file_name}] at line number: [{line_number}] with message: [{str(error)}]"



class CustomException(Exception):
    """
    Custom exception class for ML Project errors.
    """
    def __init__(self, error_message: Exception, errors_details: sys):
        self.errors_message = error_message_detail(error_message, errors_details)
        super().__init__(error_message)
        logger.error(self.errors_message)  # Logs the error using shared logger


    def __str__(self):
        return self.errors_message


# if __name__ == "__main__":
#     try:
#         1 / 0  # This will raise a ZeroDivisionError
#     except Exception as e:
#         logging.info("An error occurred, raising CustomException.")
#         raise CustomException(e, sys)
#     # The above line will raise a CustomException with detailed error information. 




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
