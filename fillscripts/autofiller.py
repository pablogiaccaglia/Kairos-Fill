# -*- coding: utf-8 -*-
import time

from nightFiller import KairosBot
import logging


def autofiller():
    kairos = KairosBot()
    kairos.start(bookingType = kairos.DOUBLE_BOOK)


if __name__ == '__main__':
    logging.basicConfig(format = '%(process)d-%(levelname)s-%(message)s', level = logging.INFO)
    logging.getLogger().setLevel(logging.INFO)
    start_time = time.time()
    autofiller()
    logging.info("--- %s seconds ---" % (time.time() - start_time))
