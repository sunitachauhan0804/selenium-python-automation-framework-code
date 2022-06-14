import inspect
import logging


def custom_logger(loglevel):
    # Set class/method name from where its called
    logger_name = inspect.stack()[1][3]
    # Create logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(loglevel)
    # 2 create console handler or file handler and set the log level
    file_handler = logging.FileHandler("..\logging_demo\logs_record.log", mode='w')
    # 3 create formatter - How you want your logs to be formatted
    formatter = logging.Formatter("%(asctime)s - %(levelname)s -%(name)s : %(message)s", datefmt="%m/%d/%y %I:%M:%S %p")
    # 4 add formatter to console or to file handler
    file_handler.setFormatter(formatter)
    # 5 add console handler to logger
    logger.addHandler(file_handler)
    # application code  - log messages
    return logger
