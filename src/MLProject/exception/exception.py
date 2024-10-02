import sys


class CustomException(Exception):
    
    def __init__(self, error_message: str, error_details: sys):
        self.error_message = error_message
        _, _, exc_tb = error_details.exc_info()
        self.lineno = exc_tb.tb_lineno
        self.filename = exc_tb.tb_frame.f_code.co_filename
    
    def __str__(self) -> str:
        return f"Error Occured in python script: {self.filename} at line: {self.lineno} with the message: {self.error_message}"
    

if __name__=="__main__":
    try:
        a=1/0

    except Exception as e:
        raise CustomException(e,sys)