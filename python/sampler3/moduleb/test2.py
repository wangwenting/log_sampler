import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def test2():
    logger.info("noshow test2")
    logger.debug("test2")
    logger.error("test2")
