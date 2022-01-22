#!/usr/bin/env python3

"""
A chronometer to schedule task.

This file is a part of python-wipbox project.

(c) 2021, Deepnox SAS.
"""

import time

import arrow


class OneMinuteChronometer(object):

    def __init__(self):
        self.current, self.next = arrow.now(), arrow.now()
        self.set_next()

    def set_next(self):
        self.next = arrow.now().replace(second=0, microsecond=0).shift(minutes=+1)

    def check(self):
        self.update_current()
        if self.current > self.next:
            self.set_next()
            return True
            # return self.current.replace(second=0, microsecond=0).format('YYYYMMDDhhmm')
        return False


    def update_current(self):
        self.current = arrow.now()

if __name__ == '__main__':
    chrono = OneMinuteChronometer()
    while True:
        time.sleep(5)
        c = chrono.check()
        if c is not None:
            print(c)