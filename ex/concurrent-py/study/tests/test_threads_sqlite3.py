#!/usr/bin/env python3

# BoBoBo

import time
import asyncio
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures._base import wait
import study.concurrent.biz_sqlite3 as biz_sqlite3


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


def test_sqlite3():
    scale = 10 ** 4
    biz_sqlite3.init()
    biz_sqlite3.write_biz('123456')

    def get_biz():

        def _biz():
            print('Read from sqlite3: %s' % biz_sqlite3.read_biz('3'))

        return _biz

    def get_asyn_biz():

        def _biz():
            print('Read from file: %s' %
                  asyncio.run(biz_sqlite3.read_biz('3')))

        return _biz

    serial_time = serial(get_biz(), scale)
    threads_time = threads(get_biz(), scale)
    eventloop_time = eventloop(get_asyn_biz(), scale)
    print('Serial do: %i Time: %s' % (scale, str(serial_time)))
    print('Threads do: %i Time: %s' % (scale, str(threads_time)))
    print('Eventloop Asyn do: %i Time: %s' % (scale, str(eventloop_time)))
