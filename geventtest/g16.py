__author__ = 'Administrator'
import gevent
from gevent import getcurrent
from gevent.pool import Pool


pool = Pool(2)



def hello_from(n):
    print('Size of pool', len(pool))



pool.map(hello_from, xrange(3))