#!/usr/bin/env python3

# BoBoBo

import asyncio
from threading import Thread
from multiprocessing import Process
from multiprocessing import Queue
import time


count = 0
t0 = time.process_time()


async def a_do_r(r):
    do_r(r)


def do_r(r):
    print("Start to exec request: %s" % str(r))
    # print(read_file(r))
    time.sleep(1)
    print("Finish to exec request: %s" % str(r))
    global count
    count += 1
    if count == 20:
        global t0
        print(str(time.process_time() - t0))
        exit(0)
    else:
        print('do: %s' % str(count))


def return_to_pipe(r):
    with open(r['trans_file'], 'w') as fo:
        print(r['path'], file=fo)


def read_file(r):
    with open(r['trans_file'], 'r') as fo:
        line = fo.readline()
    return line


def start_eventloop(request_queue):
    el = asyncio.new_event_loop()
    asyncio.set_event_loop(el)

    def _eventloop():
        nonlocal el
        asyncio.set_event_loop(el)
        el.run_forever()

    # eventloop_thread = Thread(target=_eventloop,
    #                          daemon = True)
    # eventloop_thread.start()
    while True:
        print("Wait for queue")
        worker_data = None
        try:
            worker_data = request_queue.get(timeout=1)
        except Exception as ex:
            print("Queue get timeout.")
        if worker_data:
            print("Get from queue: %s" % str(worker_data))
            coroutine = a_do_r(worker_data)
            # asyncio.run_coroutine_threadsafe(coroutine, el)
            el.run_until_complete(coroutine)


request_queue = Queue()

p = None


def start_process():
    global request_queue
    global p
    p = Process(target=start_eventloop, args=(request_queue,),
                daemon=True)
    p.start()


def do_request(request):
    print('do_request: %s' % str(request))
    global request_queue
    request_queue.put(request)


if __name__ == "__main__":
    r = {'trans_file': './test.txt', 'path': '/a/b/c'}
    #t0 = time.process_time()
    for i in range(20):
        do_r(r)
    print(time.process_time() - t0)
    """

    start_process()
    r = {'trans_file': './test.txt', 'path': '/a/b/c'}
    for i in range(20):
        do_request(r)
    p.join()
    """
