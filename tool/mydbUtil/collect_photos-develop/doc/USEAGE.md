
## 工具使用文档:

### 1. 目录说明:

    conf:
        执行环境的配置文件
    deploy:
        emCollect.conf  nginx 配置
    emCollect:
        python包目录
    log：
        运行时日志
    resource:
        城市配置  用于获取中文名,cityCode 映射关系
    alembicInit:
        用于配置   关联全局城市数据映射表所在的数据库(emTestDataCollect)
    alembic:
        用于生产环境数据迁移工作

    脚本文件:
        build.sh：
            安装环境依赖
        rebuildAlembic.sh：
            用于初次安装时：
                1. 配置 alembic.ini   以及  env.py
                2. 自动创建数据库 (conf/db.conf.json 中配置的)

    do_test.sh:
        用于 emCollect/service/   下的子包
    start.sh :
        用于正式程序


### 2. 执行入口说明:

``` shell script
./start.sh -h
USEAGE:
        python3 [projectName] [-h]  [--isRun] [--isDebug] [--sourceContent  source] [--sourceType type]

        -h                      : 帮助信息
        --isRun                 : 立即执行解压归档操作 (默认只做文件检测)
        --isDebug                       : 是否以debug日志方式进行<无进度条显示,会打印每个文件>
        --sourceContent source  : 文件/文件夹/http链接 <请使用';' 进行分割 ,(不支持三种混用)>; [example:  --source 'file1;file2;file3' ]
        --sourceType type       : source 类型名称 ; SOURCE_TYPE in '['files', 'urls', 'dirs']'

./start.sh   --sourceType 'dirs' --sourceContent '/6t/chejian/software/collectTOOL/test_tarfiles/bak1'   --isRun

```

    目前工程只支持了：
        1.zip  和  tar.gz 两种压缩格式
        2. 处理单个目录的下的第一层目录里的所有的文件
        或  处理多个压缩文件<用分号隔开>   并在执行参数里带上  --sourceContent 的类型(--sourceType)  '['files', 'urls', 'dirs']'


### 3. 执行结果说明:

    yuyang@yuyang-virtual-machine:~/develop/doc/collect_photos$ tree  ../_Data_emCollect/20201203_093724/
    ../_Data_emCollect/20201203_093724/
    ├── failure
    │   ├── rarlinux-x64-5.9.1.tar.gz
    │   └── test.tar.gz
    ├── report.txt
    └── success
        ├── chejian.tar.gz
        └── chejian.zip

    2 directories, 5 files
    
    执行完毕会生成对原始文件的归纳,并生成报告 <report.txt>
    
    现场配置,以及图片会被放到指定目录,现场数据库表,会被命名类型(emTest_chejian_4419_20200828) 的新建数据导入
    同时每个现场数据文件在 emTestDataCollect 中 会有一张 数据位置映射表:
    可支持 (拼音|汉字)名称 ,citycode, export date 检索;
    
    可通过网页查看目录树
    example:
        http://192.168.50.100:7002/rawdata/chejian/photos/4419/2020-08-28/


### 4.其他问题
#### 4.1 数据位置
     数据根目录${root_data} 是配置文件指定的 同时会关联的nginx 的配置修改
     常规数据位于  ${root_data}/  
     误判数据位于   ${root_data}/emDataWuPan/
     二者子目录格式一致

    正确的车检导出数据  原始目录格式为(查验类似):
    chejian
    ├── 4419
    │   └── 2020-08-28
    │       ├── 0111_S2682_LALPCJ932C3060442
    │       ├── 0111_S2J8B1_LVAV2JVB4HE285906
    │       ├── 0111_S3F2A5_LS4BDB3D87A169504
    └── CheJianConfig
        ├── algConfig
        │   ├── algClassConfig_4419
        │   │   ├── algClass_11.json
        │   │   ├── algClass_14.json
    
    现场的新增的网页版导出工具会严格限制导出包的格式:
    其命名如下:
    emData_chejian_4419_20210118103924_CJWP_{encodeVersion}.tar.gz
    
    1. 以 emData_ 开头
    2. 误判数据会包含 CJWP 的字样
    3. 如 encodeVersion 存在 即为原始照片进行过加密编码  含义为 加密版本号
    
    误判数据支持一天导入多次误判记录 (number 属性会依次编号)
        
##### 4.1.1 常规数据
      1.同一压缩包执行多次 ,或者, 同一城市,同一天的不同压缩包
        目前程序里会做结果覆盖处理
      2. 由于程序会在解压的同时分析目录树 所以不符合要求的压缩包 不会被解析
      
      索引表为:
      emTestDataCollect--->City_DataBaseName
    
##### 4.2 误判数据
      本工具仅支持由 最新web导出工具 导出的带有  CJWP 字段的数据. 其他因旧版导出工具 目录/数据 混乱 引发的解析失败问题,该工具不做兼容,
      如有必要 请现场使用最新web工具导出
      
      索引表为:
      emTestDataCollect--->City_DataBaseName_WuPan
      
 