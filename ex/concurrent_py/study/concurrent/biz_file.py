#!/usr/bin/env python3

# BoBoBo

import asyncio
import time
import aiofiles


def read_1line(path):
    for i in range(100):
        with open(path, 'r') as fo:
            line = fo.readline()
    # time.sleep(1)
    return line


async def a_read_1line(path):
    for i in range(100):
        async with aiofiles.open(path, mode='r') as f:
            contents = await f.read()
    # await asyncio.sleep(1)
    return contents
