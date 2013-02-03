#
# Exercise 14
#
import numpy


def compute_from_file(filename, function, sep=';'):
    """Do some mathematical operations for each row in a file

    >>> compute_from_file('data.csv', 'average')
    [...]
    >>> compute_from_file('data.csv', 'median')
    [...]
    >>> compute_from_file('data.csv', 'min')
    """
    # open using with
    with open(filename, mode='r') as data:
        results = []
        for row in data:
            results.append(function([float(num) for num in row.split(sep)]))
    # if we use with we don't need to remeber to close the file
    return results

compute_from_file('data.csv', numpy.max)


#
# Exercise 15
#
import fnmatch
import os


class Finder(object):
    def __init__(self, dirpath, match, verbose=False):
        self.found = 0
        self.analyzed = 0
        self.dirpath = dirpath
        self.match = match
        self.verbose = verbose

    @timeit
    def __call__(self):
        self.looking_for(self.dirpath)
        print "Analyzed: %d filse\nFound: %d files" % (self.analyzed, self.found)

    def looking_for(self, dirpath):
        for f in sorted(os.listdir(dirpath)):
            self.analyzed += 1
            abspath = os.path.join(dirpath, f)
            if fnmatch.fnmatch(abspath, self.match):
                self.found += 1
                if self.verbose:
                    print 'found: %s' % abspath
            if os.path.isdir(abspath):
                self.looking_for(abspath)


Finder('.', '*.py')()

