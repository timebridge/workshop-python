# -*- coding: utf-8 -*-
import time

def timeit(function):
    def timed(*args, **kargs):
        # do something before
        time_start = time.time()
        # execute the function
        result = function(*args, **kargs)
        # do something after
        time_end = time.time()
        print 'name=%r (args=%r, kargs=%r) processing time=%10.8f sec' % (function.__name__, args, kargs, time_end - time_start)
        return result

    return timed