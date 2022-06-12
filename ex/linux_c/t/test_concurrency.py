#!/usr/bin/env python3

# BoBoBo

from time import sleep
from threading import Event
from threading import Thread
from multiprocessing import Process
from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import wait
import t.gl as g
import os


def test_thread():
    def loop():
        count = 5
        while count:
            print("Python is processing in thread...")
            count -= 1
            sleep(1)

    t = Thread(target=loop, daemon=True)
    t.start()
    t.join()


def test_process():
    def loop():
        count = 5
        while count:
            print("Python is processing in process...")
            count -= 1
            sleep(1)

    p = Process(target=loop)
    p.start()


def f(x):
    count = 5
    while count:
        print("Python is processing %s in pool..." % x)
        count -= 1
        sleep(1)


def test_pool():
    def exec_pool():
        pool = Pool(2)
        pool.apply_async(f, ("f1",))
        pool.apply_async(f, ("f2",))
        pool.apply_async(f, ("f3",))
        pool.apply_async(f, ("f4",))
        pool.close()
        pool.join()

    p = Process(target=exec_pool)
    p.start()


executor = None
pool_g = None
all_task = []


def hold_process():
    count = 5
    global all_task
    while count:
        print("hold process %s" % count)
        print("all_task: %s" % len(all_task))
        sleep(5)
        count -= 1


def do_r(r):
    print("Start to exec request: %s" % str(r))

    if r[0]['trans_file'] == "":
        sleep(1)
    else:
        try:
            with os.open(r[0]['trans_file'], os.O_NONBLOCK | os.O_RDWR) as fo:
                os.write(fo, r[0]['path'].encode())
        except Exception as ex:
            print("Failed to write to file for: " % ex)

    print("Finish to exec request: %s" % str(r))


def exec_pool(requests):
    executor = ThreadPoolExecutor(max_workers=2)
    count = 10
    while count:
        count -= 1
        try:
            r = requests.pop()
            executor.submit(do_r, (r,))
        except IndexError as ex:
            print("Wait request")
            # TODO: wait
            sleep(3)


def start_process():
    p = Process(target=exec_pool, args=(g.requests,))
    p.start()


def exec_request(request):
    try:
        g.requests.append(request)
    except Exception as ex:
        print("Failed to append request for: %s" % ex)
