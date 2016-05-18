from set_logger import set_logger
from modulea.test1 import test1
from moduleb.test2 import test2
import logging
import logging.config

set_logger("test.log")

def test():
    logging.info("test")
    logging.debug("test")
    logging.error("test")
test()
test1()
test2()
