#coding=utf-8
import threading
from time import ctime,sleep

fileList=[1,'a','b',2]

aMutex=threading.Lock()

def music():
    sleep(1)
    aMutex.acquire()
    fileList.append(5)
    print "%s music %s" %(ctime(),fileList)
    aMutex.release()

def movie():
    aMutex.acquire()
    fileList.append(8)
    print "%s movie %s" %(ctime(),fileList)
    sleep(3)
    aMutex.release()
    

threads = []
t1 = threading.Thread(target=music)
threads.append(t1)
t2 = threading.Thread(target=movie)
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()

    for t in threads:
        t.join() #在主线程上，等待t进入进来，也就是等待线程t运行结束

    print "all over %s" %ctime()
