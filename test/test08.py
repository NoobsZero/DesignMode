# encoding: utf-8
"""
@file: test08.py
@time: 2021/4/8 18:02
@author: Chen
@contact: Afakerchen@em-data.com.cn
@software: PyCharm
"""
from collections import namedtuple
from timeit import timeit

import numpy as np
import pandas as pd


def myiter(d, cols=None):
    if cols is None:
        v = d.values.tolist()
        cols = d.columns.values.tolist()
    else:
        j = [d.columns.get_loc(c) for c in cols]
        v = d.values[:, j].tolist()
    n = namedtuple('MyTuple', cols)
    for line in iter(v):
        yield n(*line)


def iterfullA(d):
    return list(myiter(d))


def iterfullB(d):
    return list(d.itertuples(index=False))


def itersubA(d):
    return list(myiter(d, ['col3', 'col4', 'col5', 'col6', 'col7']))


def itersubB(d):
    return list(d[['col3', 'col4', 'col5', 'col6', 'col7']].itertuples(index=False))


res = pd.DataFrame(
    index=[10, 30, 100, 300, 1000, 3000, 10000, 30000],
    columns='iterfullA iterfullB itersubA itersubB'.split(),
    dtype=float
)

for i in res.index:
    d = pd.DataFrame(np.random.randint(10, size=(i, 10))).add_prefix('col')
    for j in res.columns:
        stmt = '{}(d)'.format(j)
        setp = 'from __main__ import d, {}'.format(j)
        res.at[i, j] = timeit(stmt, setp, number=100)

print(res.groupby(res.columns.str[4:-1], axis=1).plot(loglog=True))
