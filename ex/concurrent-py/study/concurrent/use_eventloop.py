#!/usr/bin/env python3

# BoBoBo

import asyncio
from multiprocessing import Process
from multiprocessing import Queue
from threading import Thread


async def app(request):
    print('web app do request: %s' % str(request))


class PyWorker():

    def __init__(self):
        self.loop = asyncio.new_event_loop()

    def start_event_loop(self):
        print('start event loop')
        asyncio.set_event_loop(self.loop)
        self.loop.run_forever()

    def run_app(self, worker_data):
        coroutine = app(worker_data)
        asyncio.run_coroutine_threadsafe(coroutine, self.loop)


def process_loop(queue):
    pyworker = PyWorker()
    eventloop_thread = Thread(target=pyworker.start_event_loop,
                              daemon=True)
    eventloop_thread.start()
    while True:
        worker_data = queue.get()
        pyworker.run_app(worker_data)


if __name__ == "__main__":
    queue = Queue()
    p = Process(target=process_loop, args=(queue,), daemon=True)
    p.start()
    while True:
        w = input()
        if w == 'exit':
            break
        queue.put(w)
