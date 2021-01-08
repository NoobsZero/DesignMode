# 导入pymysql模块
import datetime
import os
import pymysql
from ast import literal_eval
import pypinyin
import requests
from pymysql import ProgrammingError

chepai = ['ARU XV', 'X5', 'YAMAHA', '一汽', '万事达', '万荣', '万达', '万里', '万风', '三一', '三凌', '三力', '三威', '三星', '三机',
          '三环', '三联', '三菱', '三铃', '上元', '上喆', '上汇', '上海别克', '上海帕萨特', '上海桑塔纳', '上海波罗', '上饶', '专威', '专致',
          '世纪风', '东云', '东南', '东堡', '东宇', '东岳', '东方红', '东润', '东风', '东驹', '丝治', '中华', '中基', '中天', '中奇', '中悦',
          '中昌', '中植', '中汽', '中油', '中洁', '中联', '中誉', '中运', '中通', '中郓通', '中集', '中顺', '中鱼翔驰', '丰田', '久远', '久龙',
          '义鹰', '乘龙', '九通', '九马', '事业永盛', '云豹', '云雀', '五十铃', '五岳', '五征', '五星', '五洲龙', '五羊', '五菱', '亚中车辆',
          '亚星', '亚特重工', '享御', '京探', '京驼', '仁拓博歌', '众星', '众泰', '众骄', '传祺', '佛斯弟', '佛都圣泽', '佰斯威', '佳乐', '佳美',
          '佳郓', '依维柯', '俊风', '保时捷', '倪盛', '傲虎', '儒源', '兆鑫', '先行科技', '光亚通达', '光阳', '克罗迪', '克莱斯勒', '公羊',
          '兰博基尼', '兰德酷路泽', '兴扬', '兴邦龙', '冀东巨龙', '冀贝佳', '冀骏', '农牧', '冰熊', '凌宇', '凌志', '凌扬', '凌河', '凌派', '凤凰',
          '凯丰', '凯事成', '凯伦宾威', '凯宴', '凯尊', '凯福莱', '凯翼', '凯诺', '凯迪拉克', '凯迪捷', '凯门', '凯马', '切诺基', '利亚纳',
          '利源达', '利达', '别克', '力俊', '力帆', '力狮', '加利福尼亚', '劲扬', '劲炫', '劲越', '劳恩斯', '劳斯莱斯', '勇超', '切诺基', '现代',
          '北地', '北奔', '北斗星', '北方', '北方重工', '北起多田野', '匡山', '十通', '华专一', '华东', '华凯', '华劲', '华威翔运', '华威驰乐',
          '华宇达', '华山', '华岳兴', '华建', '华政', '华新', '华昌', '华梁', '华泰', '华盛', '华神', '华美', '华菱', '华通', '华郓达',
          '华鑫联合', '华颂', '华骏', '华鲁业兴', '华鲨', '卓运昌', '南方', '南明', '南骏', '博悦', '博斯特', '博爱', '卡升', '卡姆利', '卡雷拉',
          '厦杏三阳', '友谊', '双庆', '双机', '双环', '双达', '双龙主席', '双龙爱腾', '双龙路帝', '发现', '台福小霸王', '合加', '合客', '吉利',
          '吉奥', '吉姆尼', '吉姆西', '吉普', '吉江', '吉鲁', '同强', '同心', '名爵', '君爵', '启辰', '哈弗', '哈飞', '唐鸿重工', '唯雅诺',
          '喜马', '嘉华', '嘉宝', '嘉年华', '嘉恒', '嘉陵', '嘉龙', '固得美', '国世华邦', '国恩隆创', '国道', '圆易', '圣岳', '圣德', '圣火神',
          '圣路', '圣龙', '坤博', '坦途', '埃尔法', '城市猎豹', '塞纳', '夏利', '夏朗', '多士星', '大众', '大切诺基', '大力', '大发', '大地',
          '大宇', '大捷龙', '大汉', '大翔', '大运', '大迪', '大通', '大阳', '大马', '天利', '天威缘', '天威达', '天将雄狮', '天明', '天河',
          '天籁', '天翔', '天马', '天骏德锦', '天骏达', '太行成功', '奇瑞', '奇骏', '奋进', '奔野', '奕鸥', '奥尼斯', '奥峰', '奥德赛', '奥拓',
          '奥路卡', '奥迪', '奥铃', '威乐', '威姿', '威客', '威志', '威泰克', '威特', '威达', '威驰', '威麟', '宇田', '宇畅', '宇通', '安凯',
          '安德拉', '安旭', '安源', '安通', '宏图', '宏宙', '宏巨辉', '宏昌', '宏达', '宏运', '宏鑫通', '宗申', '宝来', '宝沃', '宝石', '宝马',
          '宝骏', '宝龙', '实力', '宣广', '宾利', '富先达', '富园', '富士', '富奇', '富恩', '富旭', '富洋达', '富豪', '富迪', '少林', '尚酷',
          '尼桑', '山花', '峰光', '川宏', '川江', '川牧', '川腾', '巡洋舰', '巨运', '希尔', '帕杰罗', '帕纳美拉', '帕菲特', '帕萨特', '帝豪',
          '常光', '常奇', '常春宇创', '广丰', '广客', '广州本田雅阁', '广州雅阁', '广恩', '广汽', '广汽菲亚特', '广爵', '广科', '广通', '庆铃',
          '康恩迪', '康飞', '延龙', '建宇', '建设', '开乐', '开武', '开沃', '开瑞', '开迪', '弘瑞通', '徐工', '德国宝马', '德宝', '思域',
          '思威', '思迪', '思铂睿', '思铭', '总裁S', '恒信', '恒同', '恒宇', '恒真', '恒通', '恩信', '悍马', '悦达', '意大利', '成事达',
          '戴德', '戴纳肯', '扬子', '扶桑', '拉古那', '拓速乐', '拓锐斯特', '指南者', '指挥官', '捷豹', '捷达', '探险者', '揽胜', '揽驰', '敬业',
          '斯卡特', '斯堪尼亚', '斯威', '斯巴鲁', '斯柯达', '斯派菲勒', '斯达', '新东日', '新兖', '新凯', '新华旭', '新大洲', '新日钢', '新甲壳虫',
          '旋风', '旌航', '旗林', '无数据', '无限', '日产', '日昕', '日野', '时代', '时韵', '时风', '昂科雷', '昊统', '昊锐', '昌河', '昌骅',
          '明威', '明航', '明锐', '易昌', '星凯龙', '星马', '春洲', '春田', '春风', '晟通', '普拉多', '普瑞维亚', '普茨迈斯特', '景阳岗', '晶锐',
          '晶马', '曙光', '曙岳', '朗逸', '朗风', '本田', '本菱', '杨嘉', '杰德', '松花江', '极东', '林晟', '林海', '林肯', '枭龙', '柯兰多',
          '柯斯达', '柳工', '柳特神力', '标致', '格仑特', '格蓝迪', '格锐', '桂林', '桑塔纳', '梁兴', '梁威', '梁宇', '梁昇', '梁翔', '梁虹',
          '梁锋', '奔驰', '梅甘娜', '森林人', '森源', '楚胜', '楚风', '楚飞', '欣意通', '欧亚', '欧兰德', '欧宝', '梁山', '欧宝雅特', '欧捷利',
          '欧旅', '欧曼', '欧洲之星', '欧美佳', '欧菲莱斯', '欧迪玛', '欧铃', '欧陆', '欧雅', '歌诗图', '正康宏泰', '武夷', '比亚迪', '欧蓝德',
          '比速', '永康', '永旋', '永耀九洲', '汇众', '汇联', '汇达', '汉兰达', '永强', '汕德卡', '江南', '江天', '江山神剑', '江特', '江环',
          '江西五十铃', '江铃', '江淮', '江骏', '沃尔沃', '沃德利', '沃顺达', '沙漠', '河海明珠', '法拉利', '波罗', '泰骋', '派力奥', '济世鑫',
          '浦沅', '海伦哲', '海德', '海格', '海狮', '海福龙', '海艾士', '海虹', '海誉', '海诺', '海鸥', '海鹏', '润知星', '渝州', '港粤',
          '湖挂', '火鸟', '炎帝', '海马', '炫威', '烈昂', '燕台', '爱知', '爱维客', '爱腾', '牧马人', '牡丹', '特运', '狮跑', '猎豹', '猛禽',
          '玉柴', '王', '玖信', '玛莎', '环球', '环达', '现代', '珠峰', '珠江', '理念', '琴岛', '瑞宜达', '瑞弗', '瑞江', '瑞路豪', '瑞郓',
          '瑞驰', '瑞麒', '瓦多奇', '田宇兴', '田达', '田野', '甲壳虫', '申沃', '申龙', '畅丰', '畅达', '白云', '皇冠', '皖北泰鑫', '皖骏',
          '盛川达', '盛润', '盟盛', '知豆', '石煤', '石盛航', '神宇', '神河', '神狐', '神行', '神鹰', '神龙', '祥郓华旭', '禅珠', '福克斯',
          '福建', '福德', '福特', '福狮', '福玺', '福田', '福达', '福迪', '福龙马', '科帕奇', '科瑞', '科迈罗', '科雷傲', '程力', '程力威',
          '粤工', '粤海', '粤龙', '粱锋', '精功', '精灵', '索兰托', '紫象', '红宇', '红岩', '红旗', '红星', '红杉', '红桥', '红荷', '红都',
          '纳智捷', '绅宝', 'Q7', '维拉克斯', '绿叶', '缤智', '羊城', '美亚', '美佳', '美日', '美洲豹', '翼凌', '翼搏', '翼虎', '翼马',
          '耀隆', '耐德兼松', '联达', '聚宝', '聚尘王', '聚运达', '胜达', '胜运', '腾势', '腾运', '自由人', '自由客', '舒驰', '舜德', '航天',
          '艾力绅', '艾尔西', '苏化', '苏通', '英伦', '英田', '英致', '英莲幫巡洋舰霸道　', '英菲尼迪', '荣威', '荣德', '莱克萨斯', '莲花', '菲亚特',
          '萌山', '萨伯', '萨博', '萬祥', '蒙丹纳', '蒙迪欧', '蓝港', '蓝瑟', '蓝速', '蓬翔', '蓬莱', '虹宇', '蛇口', '衢龙', '裕诚', '西沃',
          '观致', '解放', '讴歌', '谛艾仕', '象', '豪剑', '豪天', '豪情', '豪曼', '豪江', '豪沃', '豪泺', '豪瀚', '豪爵', '豪运', '豪进',
          '豫前通', '贝纳利', '贵士', '赛利卡', '赛宝', '赛沃', '赛特', '赛纳', '赛飞利', '赛马', '赣运', '起亚', '超人', '维特拉', '超越',
          '超雄', '跃进', '跨界高尔夫', '路之友', '路斯', '路虎', '路迎奔腾', '路飞', '轩畅', '轩逸', '轻骑', '辉煌鹏达', '辉翼', '辉腾', '辰陆',
          '达福迪', '达路', '迅速', '迅龙', '迈凯', '迈特威', '迈腾', '运力', '运腾', '远东', '远程', '迪晟源', '迪马', '迷你', '途乐', '途威',
          '途安', '途锐', '通亚达', '通华', '通家福', '通广九州', '通泰鼎盛', '通顺达', '速卡迪', '速派', '速腾', '速迈', '速通', '邦乐', '郓宇',
          '郓拓', '郓翔', '酷博', '酷威', '酷搏', '酷派', '酷路泽', '醒狮', '重汽希尔博', '野马', '金优', '金冠圣路', '金华飞顺', '金君卫',
          '金城铃木', '金多利', '金威', '金徽', '金捷', '金旅', '金望', '金杯', '金猴', '金皖', '金线岭', '金银湖', '金马', '金龙', '鑫万荣',
          '鑫宏达', '鑫永成', '鑫源', '鑫阳达', '鑫鲁骏', '钟乐', '钦机', '钦洋', '钧天', '钱江', '铁力士', '铂驰', '铃木', '铃目王', '银宝',
          '银河', '银翔', '银道', '银钢', '锋范', '锐界', '锡宇', '锣响', '长城', '长安', '长春', '闽兴', '阳光', '阿克托斯', '阿尔法',
          '阿斯顿', '阿雷斯领地', '陆嘉', '陆地巡洋舰', '霸道', '陆地方舟', '陆平机器', '陆虎', '陆锋', '陆霸', '陕汽', '陕西', '隆鑫', '雅尊',
          '雅特', '雅科仕', '雅酷', '雅阁', '雅马哈', '集瑞联合', '雨辰', '雪佛兰', '雪佛来', '雪弗兰', '雪拂兰', '雪莲冷链', '雪铁龙', '雪铁龙',
          '雷克萨斯', '雷斯特', '雷诺', '霸申特', '霸锐', '青年', '青特', '韶晖', '韶液', '顺港', '顺肇', '顺运', '领航员', '颐达', '颜山',
          '风度', '风景', '风朗', '风神', '风雅', '飞度', '飞思', '飞燕', '飞球', '飞碟', '飞驰', '飞鹰', '首达', '马自达', '驰田', '驰鹏',
          '驹王', '骊威', '骊山', '骏华兴', '骏威', '骏强', '骏王', '骏翔', '骏途达', '骏逸', '骐达', '骐铃', '骜通', '高尔夫', '鲁岳', '鲁峰',
          '鲁旭达', '鲁玺', '鲁襄', '鲁郓万通', '鲁际通', '鲁驰', '鸿宇达', '鸿怡', '鸿盛业骏', '鸿运达', '鸿雁', '鹏翔星通', '麒强', '麟州',
          '黄河', '黄海', '黑豹', '齐鲁', '齐鲁中亚', '龙亿达', '龙威事业', '龙恩', '龙挂']


def get_filelist(dir, fileCondition=''):
    """
            递归获取目录下所有后缀为jpg的路径
        :param fileCondition:
        :param dir: 指定URL是目录（'dir'）
        :return: Filelist:list URL集合
        """
    Filelist = []
    Dirlist = []
    suffix = ['log', '.log', '.DAT', '.xlsx', '.z01', '.json', '.rar', '.zip', '.cer', '.py', '.exe', '.sh', '.txt',
              '.html', '.dll', '.h', '.c',
              '.cpl', '.jsa', '.md', '.properties', '.jar', '.data', '.bfc', '.src', '.ja', '.dat', '.cfg',
              '.pf', '.gif', '.ttf', '.jfc', '.access', '.template', '.certs', '.policy', '.security', '.libraries',
              '.sym', '.idl', '.lib', '.clusters', '.conf', '.xml', '.tar', '.gz', '.csv', '.sql', '.xml_hidden',
              '.lic']
    jpglist = []
    for home, dirs, files in os.walk(dir):
        for filename in files:
            # 文件名列表，包含完整路径
            if fileCondition is 'zip':
                if filename[-3:] == 'rar' or filename[-3:] == '.gz' or filename[-3:] == 'tar' or filename[
                                                                                                 -3:] == 'zip' and (
                        'sql' not in filename):
                    Filelist.append(os.path.join(home, filename))
            elif fileCondition is 'sql':
                if 'sql' in filename:
                    Filelist.append(os.path.join(home, filename))
            elif fileCondition is 'rar':
                if filename[-3:] == 'rar':
                    Filelist.append(os.path.join(home, filename))
            elif fileCondition is 'if':
                if os.path.splitext(filename)[1] in suffix or filename[-3:] in suffix:
                    Dirlist.append(home)
                    Filelist.append(os.path.join(home, filename))
                else:
                    jpglist.append(home)
            elif fileCondition is '':
                Filelist.append(os.path.join(home, filename))
    if len(jpglist) != 0:
        print('------------------输出jpg目录结构-------------------------------')
        for _ in list(set(jpglist)):
            print(_)
        print('------------------------------------------------------------')
    if len(Dirlist) != 0:
        print('------------------输出非jpg目录结构-------------------------------')
        for i in list(set(Dirlist)):
            print(i)
        print('------------------------------------------------------------')
    return Filelist


def createTable(conn, city):
    cursor = conn.cursor()
    # # 1、插入城市
    # cursor.execute("SELECT * from cj_cities WHERE name=%s;", (list(city.values())[0]))
    # if len(cursor.fetchall()) == 0:
    #     cursor.execute("INSERT INTO cj_cities(name,created_at,updated_at) VALUES(%s,NOW(),NOW());",
    #                    (list(city.values())[0]))
    #     cursor.connection.commit()
    try:
        cursor.execute("SELECT * from cj_" + list(city.keys())[0] + "_checks;")
    except ProgrammingError:
        cursor.execute("DROP TABLE IF EXISTS `cj_" + list(city.keys())[0] + "_checks`")
        # 定义要执行的SQL语句
        sql = """
        CREATE TABLE `cj_%(city)s_checks` (
                `id` bigint(20) NOT NULL AUTO_INCREMENT,
                `jylsh` varchar(255) DEFAULT NULL,
                `jyjgbh` varchar(255) DEFAULT NULL,
                `jylb` varchar(255) DEFAULT NULL,
                `hpzl_id` int(11) DEFAULT NULL,
                `hphm` varchar(255) DEFAULT NULL,
                `clsbdh` varchar(255) DEFAULT NULL,
                `syr` varchar(255) DEFAULT NULL,
                `sjhm` varchar(255) DEFAULT NULL,
                `sxrq` varchar(255) DEFAULT NULL,
                `zzrq` varchar(255) DEFAULT NULL,
                `cllx_id` int(11) DEFAULT NULL,
                `syxz` varchar(255) DEFAULT NULL,
                `zbzl` varchar(255) DEFAULT NULL,
                `kssj` varchar(255) DEFAULT NULL,
                `jssj` varchar(255) DEFAULT NULL,
                `fdjh` varchar(255) DEFAULT NULL,
                `clpp_id` int(11) DEFAULT NULL,
                `clxh` varchar(255) DEFAULT NULL,
                `ccdjrq` varchar(255) DEFAULT NULL,
                `ccrq` varchar(255) DEFAULT NULL,
                `wgjcjyy` varchar(255) DEFAULT NULL,
                `xszbh` varchar(255) DEFAULT NULL,
                `fzrq` varchar(255) DEFAULT NULL,
                `rlzl` varchar(255) DEFAULT NULL,
                `zpzs` varchar(255) DEFAULT NULL,
                `spzs` varchar(255) DEFAULT NULL,
                `bdbhgs` int(11) DEFAULT NULL,
                `csys_id` int(11) DEFAULT NULL,
                `pl` varchar(255) DEFAULT NULL,
                `gl` varchar(255) DEFAULT NULL,
                `zxxs` varchar(255) DEFAULT NULL,
                `cwkc` varchar(255) DEFAULT NULL,
                `cwkk` varchar(255) DEFAULT NULL,
                `cwkg` varchar(255) DEFAULT NULL,
                `hxnbcd` varchar(255) DEFAULT NULL,
                `hxnbkd` varchar(255) DEFAULT NULL,
                `hxnbgd` varchar(255) DEFAULT NULL,
                `gbthps` varchar(255) DEFAULT NULL,
                `zs` varchar(255) DEFAULT NULL,
                `zj` varchar(255) DEFAULT NULL,
                `qlj` varchar(255) DEFAULT NULL,
                `hlj` varchar(255) DEFAULT NULL,
                `ltgg` varchar(255) DEFAULT NULL,
                `lts` varchar(255) DEFAULT NULL,
                `zzl` varchar(255) DEFAULT NULL,
                `hdzzl` varchar(255) DEFAULT NULL,
                `hdzk` varchar(255) DEFAULT NULL,
                `zqyzl` varchar(255) DEFAULT NULL,
                `qpzk` varchar(255) DEFAULT NULL,
                `hpzk` varchar(255) DEFAULT NULL,
                `clyt_id` int(11) DEFAULT NULL,
                `ytsx` varchar(255) DEFAULT NULL,
                `sfxny` varchar(255) DEFAULT NULL,
                `xnyzl` varchar(255) DEFAULT NULL,
                `yxqz` varchar(255) DEFAULT NULL,
                `hbdbqk` varchar(255) DEFAULT NULL,
                `qzbfqz` varchar(255) DEFAULT NULL,
                `xzqh` varchar(255) DEFAULT NULL,
                `gcjk` varchar(255) DEFAULT NULL,
                `dybj` varchar(255) DEFAULT NULL,
                `zzg` varchar(255) DEFAULT NULL,
                `clpp2` varchar(255) DEFAULT NULL,
                `jyhgbzbh` varchar(255) DEFAULT NULL,
                `sfmj` varchar(255) DEFAULT NULL,
                `zt` varchar(255) DEFAULT NULL,
                `djrq` varchar(255) DEFAULT NULL,
                `zsxzqh` varchar(255) DEFAULT NULL,
                `zzxzqh` varchar(255) DEFAULT NULL,
                `fdjxh` varchar(255) DEFAULT NULL,
                `sgcssbwqk` varchar(255) DEFAULT NULL,
                `bmjyy` varchar(255) DEFAULT NULL,
                `glbm` varchar(255) DEFAULT NULL,
                `zzcmc_id` int(11) DEFAULT NULL,
                `jylsh2` varchar(255) DEFAULT NULL,
                `is_video_check` varchar(255) DEFAULT NULL,
                `station_status` int(11) DEFAULT NULL,
                `center_status` int(11) DEFAULT NULL,
                `is_pass` int(11) DEFAULT NULL,
                `device_id` int(11) DEFAULT NULL,
                `check_created_at` datetime DEFAULT NULL,
                `created_at` TIMESTAMP DEFAULT now() COMMENT '创建时间',
                `updated_at` TIMESTAMP DEFAULT now() COMMENT '更改时间',
                PRIMARY KEY (`id`)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
            """
        sql = sql % dict(city=list(city.keys())[0])
        # 执行SQL语句
        cursor.execute(sql)
    try:
        cursor.execute("SELECT * from cj_" + list(city.keys())[0] + "_infos;")
    except ProgrammingError:
        cursor.execute("DROP TABLE IF EXISTS `cj_" + list(city.keys())[0] + "_infos`")
        # 定义要执行的SQL语句
        sql = """
        CREATE TABLE `cj_%(city)s_infos` (
            `id` int(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
            `vehicle_check_id` integer(11) DEFAULT NULL COMMENT '外键，连接vehicle_checks的主键',
            `category_id` integer(20) DEFAULT NULL COMMENT '类型ID',
            `name` varchar(255) DEFAULT NULL COMMENT '文件名',
            `result` int(10) unsigned DEFAULT NULL COMMENT '检测结果',
            `info_created_at` datetime DEFAULT NULL COMMENT '本行创建时间',
            `created_at` TIMESTAMP DEFAULT now() COMMENT '创建时间',
            `updated_at` TIMESTAMP DEFAULT now() COMMENT '更改时间',
            PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
            """
        sql = sql % dict(city=list(city.keys())[0])
        # 执行SQL语句
        cursor.execute(sql)
    cursor.close()
    return "cj_" + list(city.keys())[0] + "_checks", "cj_" + list(city.keys())[0] + "_infos"


def getSqlData(url):
    table_checks_bool = False
    table_infos_bool = False
    checks_start = "INSERT INTO `vehicle_checks` VALUES ("
    infos_start = "INSERT INTO `check_infos` VALUES ("
    end = ");"
    lis = []
    checks_lis = []
    infos_lis = []
    table_checks_lis = []
    table_infos_lis = []
    with open(url, 'rb') as fo:
        while True:
            line = fo.readline()
            if not line:
                break
            lis.append(line)
    for i in lis:
        i = i.decode(encoding='utf-8', errors="ignore").strip()
        if i.startswith("CREATE TABLE `vehicle_checks` ("):
            table_checks_bool = True
            table_infos_bool = False
        elif i.startswith("CREATE TABLE `check_infos` ("):
            table_infos_bool = True
            table_checks_bool = False
        data = i.split(' ')[0].strip('`')
        if 'COMMENT' in i and table_checks_bool and not table_infos_bool and data not in table_checks_lis:
            table_checks_lis.append(data)
        elif 'COMMENT' in i and table_infos_bool and not table_checks_bool and data not in table_infos_lis:
            table_infos_lis.append(data)
        try:
            if i.startswith(checks_start) and i.endswith(end):
                checks_data = i.lstrip(checks_start).rstrip(end)
                for v in checks_data.split('),('):
                    if v.startswith('('):
                        v = v[1:]
                    elif v.endswith(')'):
                        v = v[:-1]
                    checks = literal_eval('(' + v.replace('NULL', "'NULL'") + ')')
                    if checks not in checks_lis:
                        checks_lis.append(checks)
            elif i.startswith(infos_start) and i.endswith(end):
                infos_data = i.lstrip(infos_start).rstrip(end)
                for v in infos_data.split('),('):
                    if v.startswith('('):
                        v = v[1:]
                    elif v.endswith(')'):
                        v = v[:-1]
                    infos = literal_eval('(' + v.replace('NULL', "'NULL'") + ')')
                    if infos not in infos_lis:
                        infos_lis.append(infos)
        except SyntaxError:
            continue
    check_datas_lis = []
    for data in checks_lis:
        data = list(data)
        if len(table_checks_lis) == len(data):
            check_datas_lis.append(dict(zip(table_checks_lis, data)))
    info_datas_lis = []
    for data in infos_lis:
        data = list(data)
        if len(table_infos_lis) == len(data):
            info_datas_lis.append(dict(zip(table_infos_lis, data)))
    return check_datas_lis, info_datas_lis


def insert(conn, table, item):
    cursor = conn.cursor()
    keys = ', '.join(item[0].keys())
    values = ', '.join(['%s'] * len(item[0].keys()))
    sql = 'insert ignore into {table}({keys}) values({values})'.format(table=table, keys=keys, values=values)
    item_tup = [tuple(info.values()) for info in item]
    try:
        cursor.executemany(sql, item_tup)
        conn.commit()
        print('插入成功: %s' % table)
    except Exception as e:
        print('插入失败, 失败表名：%s' % table)
        print('失败原因：%s' % e)
        conn.rollback()
    finally:
        cursor.close()


def info_data_proce(conn, table_info_name, info_datas_lis):
    if len(info_datas_lis) != 0:
        for info in info_datas_lis:
            # 修改字段:name去掉多余字段、created_at改为info_created_at、category改为category_id
            if '/opt/vehicle/vehicle_photo' in str(info['name']):
                info['name'] = os.path.join('/', str(info['name']).lstrip('/opt/vehicle/vehicle_photo'))
            info['info_created_at'] = info.pop('created_at', None)
            cs_id = \
                literal_eval(
                    requests.get('http://192.168.50.100:3018/api/v1/chejian/get_id?field_name=city&field_value={}'
                                 .format(pinyin(cs))).text)['id']
            info['category_id'] = \
                literal_eval(
                    requests.get(
                        'http://192.168.50.100:3018/api/v1/chejian/get_id?field_name=code&city_id={}&category={'
                        '}&reason={}'
                            .format(cs_id, info.pop('category', None), info.pop('reason', None))).text)['id']
            requests.get(
                'http://192.168.50.100:3018/api/v1/chejian/get_id?field_name=riqi&city_id={}&date={}'
                    .format(cs_id, [i for i in info['name'].split('/') if validate(i)]))
        insert(conn, table_info_name, info_datas_lis)


def getChepai(clpp, chepai):
    for k in chepai:
        if clpp in k:
            return k


def check_data_proce(conn, table_check_name, check_datas_lis):
    if len(check_datas_lis) != 0:
        for check in check_datas_lis:
            # `fzjg`,`hphm`合并为hphm
            check['hphm'] = str(check.pop('fzjg', '')[:1]) + check['hphm']
            check['check_created_at'] = check.pop('created_at', None)
            # clpp 前两个字，发到接口value
            requests.get(
                'http://192.168.50.100:3018/api/v1/chejian/get_id?field_name=clpp&field_value={}'
                    .format(getChepai(check['clpp'][:2], chepai)))
            # 删除字段
            del_key_lis = ['ckbdzplist', 'zplist', 'splist', 'bdbhglist']
            for delkey in del_key_lis:
                check.pop(delkey, None)
            # 修改字段
            keybyid_lis = ['hpzl', 'csys', 'zzcmc', 'clyt', 'clpp', 'cllx']
            for key in keybyid_lis:
                check[key + '_id'] = \
                    literal_eval(
                        requests.get(
                            'http://192.168.50.100:3018//api/v1/chejian/get_id?field_name={}&field_value={}'
                                .format(key, check.pop(key, None))).text)['id']
        insert(conn, table_check_name, check_datas_lis)


def pinyin(word):
    """
        中文转拼音
    :param word: 中文
    :return: 拼音
    """
    s = ''
    for i in pypinyin.pinyin(word, style=pypinyin.NORMAL):
        s += ''.join(i)
    return s


def is_all_chinese(strs):
    """
        判断是否是中文
    :param strs:
    :return:
    """
    for _char in strs:
        if not '\u4e00' <= _char <= '\u9fa5':
            return False
    return True


def is_odd(n):
    """
        filter过滤
    :param n:
    :return:
    """
    return 'info' not in n


def validate(date_text):
    """
        时间检验
    :param date_text:
    :return:
    """
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        re = True
    except ValueError:
        re = False
    return re


if __name__ == '__main__':
    with open(r"E:\dbsql\sqlurl.txt", 'r', encoding='utf-8', errors="ignore") as f:
        data = [line.strip('\n') for line in f.readlines()]
    urlpath = r'\\192.168.90.10\data\chejian\chejian'
    for cy in os.listdir(urlpath):
        cy_url = os.path.join(urlpath, cy, 'sql')
        if os.path.isdir(cy_url):
            sqlurls = list(filter(is_odd, get_filelist(cy_url, 'sql')))
            for sqlurl in sqlurls:
                if sqlurl not in data:
                    cs = sqlurl.lstrip(r'\\192.168.90.10\data\chejian\chejian').split('\\')[0]
                    print(sqlurl)
                    check_datas_lis, info_datas_lis = getSqlData(sqlurl)
                    # print("连接database")
                    conn = pymysql.connect(host='192.168.50.100', user='root', password='EmDataMysql2020###',
                                           database='em_vehicle', charset='utf8')
                    # print("创建表")
                    city = {pinyin(cs): cs}
                    table_check_name, table_info_name = createTable(conn, city)
                    # print("info数据清洗")
                    info_data_proce(conn, table_info_name, info_datas_lis)
                    # print("check数据清洗")
                    check_data_proce(conn, table_check_name, check_datas_lis)
                    print("关闭数据库连接")
                    conn.close()
                    with open(r"E:\dbsql\sqlurl.txt", 'w', encoding='utf-8', errors="ignore") as fo:
                        fo.write(sqlurl + '\n')
                        fo.flush()
