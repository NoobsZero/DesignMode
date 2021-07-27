# encoding: utf-8
"""
@file: test.py
@time: 2021/7/16 15:40
@author: Chen
@contact: Afakerchen@em-data.com.cn
@software: PyCharm
"""
from enum import Enum

import uvicorn
from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()


@app.get("/")
def hello():
    return {"Hello": "World"}


@app.get('/transform')
async def getCocoJson(data_type: str, img_path: str, data_path: str, local_path: str, coco_img_path: str = None):
    if coco_img_path is None:
        coco_img_path = img_path
    return {'data_type': data_type}


@app.post('/user/update')
async def update_user(*, user_id: int, really_update: int = Query(...)):
    return {'user_id': user_id}


class TfDataType(Enum):
    JSON = 'json'
    XML = 'xml'


if __name__ == '__main__':
    Tf = {TfDataType.JSON: 'json', TfDataType.XML: 'xml'}
    print(TfDataType)
    # docs redoc
    # uvicorn.run(app=app, host="127.0.0.1", port=8000)
