# -*- coding: utf-8 -*-
import time
import schedule as schedule

from nightFiller import KairosBot


# sched = BlockingScheduler()

def autofiller():
    kairos = KairosBot()
    kairos.start(bookingType = kairos.DOUBLE_BOOK)


# schedule.every().day.at("00:01").do(autofiller)

if __name__ == '__main__':
    # while True:
    #     schedule.run_pending()
    #  print("hello")
    #     time.sleep(1)
    start_time = time.time()
    autofiller()
    print("--- %s seconds ---" % (time.time() - start_time))

