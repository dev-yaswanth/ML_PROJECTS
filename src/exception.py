import sys

# Whenever an error raises we need to call this function. So we are creating a class also below.
# whenever some error occurred we get this message as we are using this class in try catch blocks.


def error_message_details(
    error, error_detail: sys
):  # error_detail:sys here we can also write like error_detail , sys not required.
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occurred in python script file name [{0}] at line number [{1}] and error message is [{2}] ".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)  # we are inheriting the init function
        self.error_message = error_message_details(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        return self.error_message




if __name__ == "__main__":
    import logging        # use logging
    import src.logger     # configure logging
    logging.info('Testing exception module')
    try:
        a = 10 / 0
    except Exception as e:

        # raise CustomException(e,sys) this stops the program wih error
        err = CustomException(e, sys)
        print(err)
        logging.error(err)
