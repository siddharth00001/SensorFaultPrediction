import sys
from logger import logging

def exceptionHandler(error,error_detail:sys)->str:
    _,_,exc_tb = error_detail.exc_info()
    file_name  = exc_tb.tb_frame.f_code.co_filename
    error_message =f"\n Error occured in the file {file_name} line no {exc_tb.tb_lineno} error {str(error)}"
    return error_message
class CustomExceptionHandling(Exception):
    def __init__(self,error_message,error_detail:sys):
        """
        param error_message: returns error message in string format
        """
        super().__init__(error_message)
        self.error_message = exceptionHandler(error_message,error_detail=error_detail)
    
    def __str__(self)->str:
        return self.error_message

if __name__ =="__main__":
    try:
        print(1/0)
        logging.info('Code worked fine - test1')
        logging.shutdown()
    except Exception as e:
        logging.info(f'Exception {str(e)} happend -test1')
        logging.shutdown()
        raise CustomExceptionHandling(e,sys)