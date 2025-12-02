"""logger.py
Simple logger wrapper (placeholder).
"""

import logging


def get_logger(name=__name__):
    logger = logging.getLogger(name)
    if not logger.handlers:
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)
    return logger


if __name__ == "__main__":
    log = get_logger()
    log.info("logger placeholder")
