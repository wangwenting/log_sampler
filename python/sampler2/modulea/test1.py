import logging

logger = logging.getLogger("aaa")
logger.setLevel(logging.DEBUG)
#filter_ = logging.Filter("module")
#logger.addFilter(filter_)

def test1():
    logger.info("logger test1")
    logger.debug("logger test1")
    logger.error("logger test1")
    logging.info("root test1")
