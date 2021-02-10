import os, sys, getopt
import logging


SOURCE_TYPE_FILES = 'files'
SOURCE_TYPE_URLS = 'urls'
SOURCE_TYPE_DIRS = 'dirs'

SOURCE_TYPE_NAME=[SOURCE_TYPE_FILES,SOURCE_TYPE_URLS,SOURCE_TYPE_DIRS]

class ReadCommandParameter:
    def __init__(self):
        self.logLevel = logging.INFO
        self.isRun  = False
        self.sourceStr = ""
        self.sourceType = ""
        self.sourceData = []
        self.noMove = False
        # self.sourceDirs = []
        # self.sourceLocalFiles=[]
        # self.sourceHttpFiles=[]

    def UseAge(self):
        print("")
        print ("USEAGE:")
        print("\tpython3 [projectName] [-h]  [--isRun] [--isDebug] [--noMove] [--sourceContent  source] [--sourceType type]  ")
        print("\t")
        print("\t-h\t\t\t: 帮助信息")
        print("\t--isRun\t\t\t: 立即执行解压归档操作 (默认只做文件检测) ")
        print("\t--isDebug\t\t\t: 是否以debug日志方式进行<无进度条显示,会打印每个文件>")
        print("\t--noMove\t\t\t: 不移动原始文件 到 归档目录 ")
        print("\t--sourceContent source \t: 文件/文件夹/http链接 <请使用';' 进行分割 ,(不支持三种混用)>; [example:  --source 'file1;file2;file3' ]")
        print("\t--sourceType type \t: source 类型名称 ; SOURCE_TYPE in '{}'".format(SOURCE_TYPE_NAME))

        print("")

    def parseCommandArgs(self, argv):
        # print argv
        try:
            opts, args = getopt.getopt(argv, "hc:t:", ["sourceType=","sourceContent=", "isDebug","isRun","noMove"])
        except getopt.GetoptError:
            self.UseAge()
            sys.exit(2)

        #print(opts)
        for opt, arg in opts:
            if opt == '-h':
                self.UseAge()
                sys.exit()
            elif opt in ("--sourceType"):
                self.sourceType = arg
            elif opt in ("--sourceContent"):
                self.sourceStr = arg
            elif opt in ("--isDebug"):
                self.logLevel = logging.DEBUG
            elif opt in ("--isRun"):
                self.isRun = True
            elif opt in ("--noMove"):
                self.noMove = True

        if not self.sourceType in SOURCE_TYPE_NAME:
            print("sourceType[{}] is not in {}".format(self.sourceType,SOURCE_TYPE_NAME))
            sys.exit(1)

        self.sourceData = [ item for item in self.sourceStr.split(";") if len(item) > 0 ]
        self.printInputMessage()
        return self

    def  printInputMessage(self):
        print(self.__dict__)


if __name__ == "__main__":
    commandParam = ReadCommandParameter()
    commandParam.parseCommandArgs(sys.argv[1:])
