#!/usr/bin/env python3

# BoBoBo

import time
import asyncio
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures._base import wait
import study.concurrent.biz_file as biz


def serial(biz, scale):
    t0 = time.time()
    for i in range(scale):
        biz()
        print('Serial biz: %i' % i)
    return time.time() - t0


def threads(biz, scale):
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=10) as pool:
        future_list = [pool.submit(biz) for i in range(scale)]
        wait(future_list)
    return time.time() - t0


def eventloop(biz, scale):
    t0 = time.time()

    el = asyncio.new_event_loop()

    async def _all_task(loop):
        nonlocal biz
        nonlocal scale
        for i in range(scale):
            loop.call_soon(biz)

    el.run_until_complete(_all_task(el))
    el.close()

    return time.time() - t0


def test_contrast():
    scale = 10**1

    def get_biz():
        file_path = './test.txt'

        def _biz():
            nonlocal file_path
            print('Read from file: %s' % biz.read_1line(file_path))

        return _biz

    def get_asyn_biz():
        file_path = './test.txt'

        def _biz():
            nonlocal file_path
            print('Read from file: %s' %
                  asyncio.run(biz.a_read_1line(file_path)))

        return _biz

    serial_time = serial(get_biz(), scale)
    serial_asyn_time = serial(get_asyn_biz(), scale)
    threads_time = threads(get_biz(), scale)
    threads_asyn_time = threads(get_asyn_biz(), scale)
    eventloop_time = eventloop(get_asyn_biz(), scale)

    print('Serial do: %i Time: %s' % (scale, str(serial_time)))
    print('Serial Asyn do: %i Time: %s' % (scale, str(serial_asyn_time)))
    print('Threads do: %i Time: %s' % (scale, str(threads_time)))
    print('Threads Asyn do: %i Time: %s' % (scale, str(threads_asyn_time)))
    print('Eventloop Asyn do: %i Time: %s' % (scale, str(eventloop_time)))
