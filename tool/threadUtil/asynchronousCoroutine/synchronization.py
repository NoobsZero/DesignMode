# encoding: utf-8
"""
@file: synchronization.py
@time: 2021/6/21 11:27
@author: Chen
@contact: Afakerchen@em-data.com.cn
@software: PyCharm
"""
# import asyncio
# import requests
# import time
#
# start = time.time()
#
#
# async def request():
#     url = 'http://127.0.0.1:5000'
#     print('Waiting for', url)
#     response = requests.get(url)
#     print('Get response from', url, 'Result:', response.text)
#
#
# if __name__ == '__main__':
#     # 单进程（协程）
#     tasks = [asyncio.ensure_future(request()) for _ in range(5)]
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(asyncio.wait(tasks))
#     # 10.127456665039062
#     # for _ in range(5):
#     #     request()
#
#     end = time.time()
#     print('Cost time:', end - start)

# import asyncio
# import aiohttp
# import time
#
# start = time.time()
#
#
# async def get(url):
#     session = aiohttp.ClientSession()
#     response = await session.get(url)
#     result = await response.text()
#     await session.close()
#     return result
#
#
# async def request():
#     url = 'http://127.0.0.1:5000'
#     print('Waiting for', url)
#     result = await get(url)
#     print('Get response from', url, 'Result:', result)
#
#
# if __name__ == '__main__':
#     # 异步协程
#     tasks = [asyncio.ensure_future(request()) for _ in range(5)]
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(asyncio.wait(tasks))
#     end = time.time()
#     print('Cost time:', end - start)

# import requests
# import time
# import multiprocessing
#
# start = time.time()
#
#
# def request(_):
#     url = 'http://127.0.0.1:5000'
#     print('Waiting for', url)
#     result = requests.get(url).text
#     print('Get response from', url, 'Result:', result)
#
#
# if __name__ == '__main__':
#     # 多进程
#     cpu_count = multiprocessing.cpu_count()
#     print('Cpu count:', cpu_count)
#     pool = multiprocessing.Pool(cpu_count)
#     pool.map(request, range(5))
#     end = time.time()
#     print('Cost time:', end - start)

import asyncio
import aiohttp
import time
from aiomultiprocess import Pool


async def get(url):
    session = aiohttp.ClientSession()
    response = await session.get(url)
    result = await response.text()
    await session.close()
    return result


async def request():
    url = 'http://127.0.0.1:5000'
    urls = [url for _ in range(5)]
    async with Pool() as pool:
        result = await pool.map(get, urls)
        return result


if __name__ == '__main__':
    start = time.time()
    # 异步与多进程的结合
    coroutine = request()
    task = asyncio.ensure_future(coroutine)
    loop = asyncio.get_event_loop()
    re = loop.run_until_complete(task)
    end = time.time()
    print(re)
    print('Cost time:', end - start)
