
工具开发文档:

## model 模块:

    使用 sqlalchemy orm 框架, 迁移工具使用 alembic

    #https://blog.csdn.net/aimill/article/details/82152173
    #https://www.cnblogs.com/chnmig/p/10446346.html
    #迁移过程
    #https://www.cnblogs.com/john-xiong/p/13650555.html

    其他常用命令:

    alembic -h
    当orm 表格有改动字段 通常需要做以下操作:
    1.如果不熟悉工具,请做下数据库内容备份

    2.
    alembic revision --autogenerate -m 'your_describe'
    alembic history  :可看到新增项

    执行这一步之后请检查 并手动修改 升级函数,降级函数

    3.执行升级
    alembic upgrade head


## common：
    基础功能封装


## service:
    parseCommand.py           命令行解析
    parseConf.py              解压目录操作
    unCompressCenter.py       批量解压封装;映射表数据生成;报告生成
    unCompressFunc.py         压缩包解析分装
    unCompressItem.py         单个压缩包解压

