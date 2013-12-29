'''
Created on 2013.12.29.

@author: zolka
'''
import queue
import threading
import time
import random
import datetime
import webbrowser
import urllib.request

def main():
    n = 1600
    startTime = datetime.datetime.now()
    q = queue.Queue()
    threads = []
    
    for i in range(0,n):
        t = threading.Thread(target=async_shit, args=(q, i))
        t.daemon = False
        threads.append(t)
        
    [x.start() for x in threads]
    [x.join() for x in threads]
    
    sum = 0
    while(not q.empty()):
        sum += q.get()
        
    print("Success rate: " + str(100*sum/n) + "%, (" + str(sum) + "/" + str(n) + ")")
    print("Finished in: " + str(datetime.datetime.now() - startTime))
    
def async_shit(q, i):
    #rnd = random.random()
    #time.sleep(rnd)
    #print("thread"+str(i)+" w/ timeout: "+str(rnd))
    
    try:
        with urllib.request.urlopen("http://hajnalgroup.com") as url:
            s = url.read()
        q.put(1)
    except Exception as e: 
        q.put(0)
        print("Thread" + str(i) + " failed: " + str(e))

if __name__ == '__main__':
    main()