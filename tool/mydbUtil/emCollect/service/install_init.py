
from ..common.baseConfig_ini import *
from ..common.baseDBOperate import *



def startInit():
    dbconfigPath = "./conf/db.conf.json"
    createDataBase(dbconfigPath)

    sourceStr = DbConfigure(dbconfigPath).getSource()
    setConfigIni("./alembic.ini",[("alembic","sqlalchemy.url",sourceStr)])

if __name__ == '__main__':
    startInit()
