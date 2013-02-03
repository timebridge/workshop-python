

#
# Exercise 8
#
def divide(numerator, denominator):
    try:
        return numerator / denominator
    except ZeroDivisionError:
        print "Divide a number with 0 is not a valid operation!"
    except TypeError:
        print 'Not a valid parameter!'


#
# Exercise 9
#

def args_kargs(*args, **kargs):
    for arg in args:
        print 'arg:', arg
    for key, val in kargs.items():
        print 'karg[%s]: %r' % (key, val)
