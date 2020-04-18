import requests
import threading
import queue
import time
"""1. 使用多线程写一个并发http，get请求的程序，
可设置并发数和请求总数，返回请求状态码
"""



req_count = 4  # 请求数
thread_count = 10  # 线程数
dataQueue = queue.Queue()
lock = threading.Lock()


def req_pro(req_count):
    for i in range(req_count):
        url = "http://www.baidu.com"
        dataQueue.put(requests.get(url).status_code)


def con_req(req_count):
    while True:
        try:
            data = dataQueue.get(block=False)  # True时会一直等待，队列为空没有可消费的不会也不会退出
        except queue.Empty:
            break
        with lock:
            print("请求数", req_count, " ==> ", data)
        time.sleep(0.1)
        dataQueue.task_done()

if __name__ =="__main__":
    pro_threads = []
    con_threads = []
    # 生产run
    for i in range(thread_count):
        t = threading.Thread(target=req_pro, args=(req_count,))
        pro_threads.append(t)
        t.start()
    for l in pro_threads:
        l.join()
    # 消费run
    for i in range(thread_count):
        t = threading.Thread(target=con_req, args=(req_count,))
        con_threads.append(t)
        t.start()
    for l in con_threads:
        l.join()



"""2. 使用多进程写一个并发http，get请求的程序， 可设置并发数和请求总数，返回请求状态码"""
from multiprocessing import Process, Lock
req_counts = 4
process_num = 10
url = "http://www.baidu.com"

def req_http(req_count, lock):
    with lock:
        for i in range(req_count):
            res = requests.get(url)
            print(res.status_code)

if __name__ == "__main__":
    process_j = []
    lock = Lock()
    for i in range(process_num):
        p = Process(target=req_http, args=(req_count, process_num))
        process_j.append(p)
        p.start()

    for j in process_j:
        j.join()