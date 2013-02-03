#
# Exercise 7
#
contact = {'pietro': 333123808, 'jonh': 123123123}

[(key, contact[key]) for key in contact.keys()]
contact.items()
[item for item in contact.iteritems()]


#
# Exercise 8
#
def divide(numerator, denominator):
    try:
        print numerator / denominator
    except ZeroDivisionError:
        print "Divide a number with 0 is not a valid operation!"
    except TypeError:
        print "Not a valid parameter!"


#
# Exercise 9
#
def args_kargs(*args, **kargs):
    for arg in args:
        print 'arg: %r' % arg
    for key, value in kargs.iteritems():
        print 'karg[%s]: %r' % (key, value)
