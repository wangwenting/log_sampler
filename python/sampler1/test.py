import logging
from logging import config
import LOGGING 
from modulea.test1 import test1
from moduleb.test2 import test2

config.dictConfig(LOGGING.LOGGING)

def test():
    logging.info("test")
    logging.debug("test")
    logging.error("test")
test()
test1()
test2()


