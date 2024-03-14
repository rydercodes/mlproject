import sys
import logging
import os

def error_message_detail(message, message_detail:None):
    _, _, exc_tb = sys.exc_info()  # Directly use sys.exc_info() as message_detail might not be the correct way to pass it
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"{message} in {file_name} at line {exc_tb.tb_lineno}"

    return error_message

class CustomException(Exception):
    def __init__(self, error_message, message_detail=None):
        self.error_message = error_message_detail(error_message, message_detail)
        super().__init__(self.error_message)

    def __str__(self):
        return self.error_message
