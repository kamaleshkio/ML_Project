import sys

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb=error_detail.exc_info(())
    file_name= exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name[{0}] line number[{1}] error message[{2}]".format(
     file_name, exc_tb.tb_lineno, str(error))
    return error_message



class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys): # Constructor or Initializer
        super().__init__(error_message) # Call the base class constructor with the parameters it needs
        self.error_message = error_message_detail(error_message, error_detail=error_detail) # Set the error message
        
    def __str__(self): # __str__ is a special method that is called when the object is printed
        return self.error_message # Return the error message
    
