# encoding: utf-8
"""
@file: test01.py
@time: 2021/6/21 15:12
@author: Chen
@contact: Afakerchen@em-data.com.cn
@software: PyCharm
"""
# 使用协程
import aiohttp
import asyncio
import time

from aiomultiprocess import Pool


async def other_test(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            result = await response.text(encoding="utf-8")
            return result


async def test2(urls):
    async with Pool() as pool:
        result = await pool.map(other_test, urls)
        return result


if __name__ == '__main__':
    urls = ["https://segmentfault.com/p/1210000013564725",
            "https://www.jianshu.com/p/83badc8028bd",
            "https://www.baidu.com/"]
    start = time.time()
    coroutine = test2(urls)
    task = asyncio.ensure_future(coroutine)
    loop = asyncio.get_event_loop()
    re = loop.run_until_complete(task)
    end = time.time()
    for i in re:
        print(i)
    print('Cost time:', end - start)
