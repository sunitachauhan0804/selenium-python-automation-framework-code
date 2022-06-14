import logging


class LoggerDemo:
    def logger_demo(self, ):
        # 1 create logger
        # logger = logging.getLogger("__ name__")  # name of the logger
        # name of the logger class(06/08/22 12:27:33 AM - DEBUG -LoggerDemo : it's a debug  logger)
        logger = logging.getLogger(LoggerDemo.__name__)
        logger.setLevel(logging.DEBUG)
        # 2 create console handler or file handler and set the log level
        console_handler = logging.StreamHandler()
        file_handler = logging.FileHandler("logs_file.log")
        # 3 create formatter - How you want your logs to be formatted
        formatter1 = logging.Formatter("%(asctime)s - %(levelname)s -%(name)s : %(message)s",
                                       datefmt="%m/%d/%y %I:%M:%S %p")
        formatter2 = logging.Formatter("%(asctime)s - %(levelname)s -%(name)s : %(message)s",
                                       datefmt="%m/%d/%y %I:%M:%S %p")
        # 4 add formatter to console or to file handler
        console_handler.setFormatter(formatter1)
        file_handler.setFormatter(formatter2)

        # 5 add console handler to logger
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
        # application code  - log messages

# logging.basicConfig(level=logging.DEBUG, filename="logs_record.log", filemode="w",
#                  format="%(asctime)s - %(levelname)s : %(message)s", datefmt="%m/%d/%y %I:%M:%S %p")

        logger.debug("it's a debug  logger")
        logger.info("info")
        logger.warning("it's a warning log")
        logger.error("error")
        logger.critical("critical")


lh = LoggerDemo
lh.logger_demo()
