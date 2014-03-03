__author__ = 'Administrator'
import multiprocessing


def producer(ns, event):
    ns.value = 'This is the value'
    event.set()



def consumer(ns, event):
    try:
        value = ns.value
    except Exception, err:
        print 'Before event, consumer got:', str(err)
    event.wait()
    print 'After event, consumer got:', ns.value



if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    namespace = mgr.Namespace()  #通过Manager管理共享命名空间
    event = multiprocessing.Event()
    p = multiprocessing.Process(target=producer, args=(namespace, event))
    c = multiprocessing.Process(target=consumer, args=(namespace, event))



    c.start()
    p.start()



    c.join()
    p.join()