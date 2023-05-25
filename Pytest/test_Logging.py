import logging


def test_logging():
    logger = logging.getLogger(__name__)   # test case name in bracket

    filehandler = logging.FileHandler('logfile.log')   # this is file location and new log file will be created

    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    filehandler.setFormatter(formatter)   # giving format info to filehandler object

    logger.addHandler(filehandler)    # pass the file location object to addHandler method so that logger object
                                      # will know where to print

    logger.setLevel(logging.WARNING)    # this will print error and critical messages only
    logger.debug("debug statement")    # these 5 types will just print messages
    logger.info("information")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical")

