import inspect
import logging


class BaseClass:

    def getlogger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)  # test case name in bracket

        filehandler = logging.FileHandler('logfile.log')  # this is file location and new log file will be created

        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)  # giving format info to filehandler object

        logger.addHandler(filehandler)  # pass the file location object to addHandler method so that logger object
        # will know where to print

        logger.setLevel(logging.DEBUG)  # this will print error and critical messages only
        return logger


