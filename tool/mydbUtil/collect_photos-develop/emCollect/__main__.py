#!/usr/bin/python3
import sys
import os

if not __package__:
    path = os.path.join(os.path.dirname(__file__), os.pardir)
    print("@@@@@@@@@@@@@@@@@@@@",path)
    sys.path.insert(0, path)
#from emCheJianRenameTool.dataSearch import *
from emCollect.service.unCompressCenter import main

##main(sys.argv[1:])
##print("---------------------------------------the end-----------------------------------")
main(sys.argv[1:])