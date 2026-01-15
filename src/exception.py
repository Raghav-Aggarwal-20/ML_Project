import sys
from src.logger import logging
from typing import Any

def error_message_detail(error: Exception, error_detail: Any) -> str:
    """Build a detailed error message using the traceback info from error_detail.

    Parameters:
    - error: the original exception or error message
    - error_detail: module providing exc_info() (typically the `sys` module)
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = (
        f"Error occurred in python script name [{file_name}] "
        f"line number [{exc_tb.tb_lineno}] error message [{str(error)}]"
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error_message: Exception, error_detail: Any):
        super().__init__(error_message)
        # store a detailed, human readable message
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self) -> str:
        return self.error_message
    
