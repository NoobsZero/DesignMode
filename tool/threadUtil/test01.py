# encoding: utf-8
"""
@file: test01.py
@time: 2021/6/18 16:05
@author: Chen
@contact: Afakerchen@em-data.com.cn
@software: PyCharm
"""
import aiohttp
import asyncio
import time
from concurrent.futures import ThreadPoolExecutor


async def request(num):
    async with aiohttp.ClientSession() as client:
        print(num)
        resp = await client.get(f'http://python.org/')
        sync_calc_fib(36)
        # resp_json = await resp.json()
        print(resp)


def sync_calc_fib(n):
    if n in [1, 2]:
        return 1
    return sync_calc_fib(n - 1) + sync_calc_fib(n - 2)


def calc_fib(n):
    print("2")
    result = sync_calc_fib(n)
    print(f'第 {n} 项计算完成，结果是：{result}')
    return result

# async def calc_fib(n):
#     print("2")
#     result = sync_calc_fib(n)
#     print(f'第 {n} 项计算完成，结果是：{result}')
#     return result


async def main():
    start = time.perf_counter()
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor(max_workers=4) as executor:
        tasks_list = [
            loop.run_in_executor(executor, calc_fib, 36),
            asyncio.create_task(request(1))
        ]
    # tasks_list = [
    #     asyncio.create_task(request()),
    #     asyncio.create_task(calc_fib(36))
    # ]
    await asyncio.gather(*tasks_list)
    end = time.perf_counter()
    print(f'总计耗时：{end - start}')

asyncio.run(main())
