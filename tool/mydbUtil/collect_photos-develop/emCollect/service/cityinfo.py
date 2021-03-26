from ..common.baselog import *


class CityNameMapper:
    def __init__(self, filePath):
        self.cityConfPath = filePath
        self.cityMapper = {}
        self.readCityName()

    def readCityName(self):
        with open(self.cityConfPath) as f:
            for item in f.readlines():
                # print("###:",item)
                li = item.strip('\n').split("\t")
                # print(li)
                self.cityMapper[li[2]] = li[0]

    def getCityName(self, citycode):
        cityName = ""
        try:
            cityName = self.cityMapper[citycode]
        except KeyError:
            logger.error("未知的citycode：[{}]".format(citycode))
        return cityName


cityMapper = CityNameMapper("./resource/citylist.txt")

if __name__ == '__main__':
    print(cityMapper.getCityName("6101"))
    print(cityMapper.getCityName("61010"))
    pass
