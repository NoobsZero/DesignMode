import json
import os
import time
from typing import List

import uvicorn
from typing import Optional
from fastapi import FastAPI, File, UploadFile, Header

app = FastAPI()


@app.post("/upload")
async def file_upload(file: List[UploadFile] = File(...)):
    print('-- align_uploadfile')
    print([file.filename for file in file])
    # a_content = file  # 接收到的是 bytes，不需要 read
    # a_path = 'a.jpg'
    # with open(a_path, 'wb') as f:
    #     f.write(a_content)
    # dict = {
    #         'a_filesize': len(a_content),
    #     }
    # return json.dumps(dict)

if __name__ == "__main__":
    # uvicorn.run(app=app, host="192.168.41.69", port=8001)
    print(os.path.abspath('.'))
