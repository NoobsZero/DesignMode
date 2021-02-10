import shutil
import os
from .baseTool import checkDir
class rawDataDecode:
    def rewrite(self,src,dst):
        with open(src, 'rb') as fsrc:
            with open(dst, 'wb') as fdst:
                shutil.copyfileobj(fsrc, fdst)

class rawDataDecode_v001(rawDataDecode):
    def __init__(self):
        print("return rawDataDecode_v001")
        pass
    def rewrite(self,src,dst):
        with open(src, 'rb') as fsrc:
            with open(dst, 'wb') as fdst:
                offset=10
                data = fsrc.seek(10)
                shutil.copyfileobj(fsrc, fdst)


rawDecodeMapper={
    "001":rawDataDecode_v001()
}
def getRawDecodeObj(version=""):
    lowver=version.lower()
    if lowver in rawDecodeMapper:
        return  rawDecodeMapper[lowver]
    return rawDataDecode()


def convertCodeData(srcDir,dstDir,version):
    checkDir(dstDir)
    decObj=getRawDecodeObj(version)
    for _,_,files in os.walk(srcDir):
        for item in files:
            print(item)
            if item.endswith(".sql") :
                continue
            decObj.rewrite(srcDir+"/"+item , dstDir+"/"+item )

if __name__ == '__main__':
    convertCodeData("/home/yuyang/develop/doc/test", "/home/yuyang/develop/doc/test2","001");
    # hd=getRawDecodeObj("V.001")
    # filesrc="/home/yuyang/develop/doc/test/test_0111_AQL932.jpg"
    # filedst="/home/yuyang/develop/doc/test/decode_test_0111_AQL932.jpg"
    # hd.rewrite(filesrc,filedst)