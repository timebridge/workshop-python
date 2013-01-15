# -*- coding: utf-8 -*-
import time
from sys import stdout

def update_progress(rest, label=None, rowbar=30):
    if label is None:
        label = '%d%%' % int(rest * 100)
    stdout.write('\r%d%% [%s%s] %s' % (int(rest * 100.),
                                       '#' * int(rest * rowbar),
                                       '-' * int((1 - rest) * rowbar),
                                       label))
    stdout.flush()


class Timer(object):
    def __init__(self, minutes=0, seconds=0):
        self.minutes = minutes
        self.seconds = seconds
        self.wait = 0.1

    def __call__(self):
        tot = self.minutes * 60 + self.seconds
        start = time.time()
        passed = 0
        while passed < tot:
            time.sleep(self.wait)
            passed = time.time() -start
            #import pdb; pdb.set_trace()
            rest = tot - passed
            if rest > 60:
                label = "Time: %dm %ds" % (rest // 60, rest % 60)
            else:
                label = "Time: %ds    " % rest
            update_progress(rest/tot, label)
        stdout.write('\n')


#min1 = Timer(1, 10)
#min1()
