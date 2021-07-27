import csv
import json

from flask import Flask

# 把当前的python文件当做一个服务
app = Flask(__name__)


# 返回请求失败数据
def is_net(return_dict):
    return_dict['return_code'] = '5004'
    return_dict['return_info'] = '请求参数为空'
    return json.dumps(return_dict, ensure_ascii=False)


# 只接受get方法访问
@app.route("/test", methods=["GET"])
def check():
    # 默认返回内容
    return_dict = {'return_code': '200', 'return_info': '请求成功', 'result': 'data'}
    # 获取传入的参数
    # 设置需要请求的必须参数（请求参数需要修改）
    # one = 'id'
    # two = 'age'
    # ID = request.args.get(one)
    # age = request.args.get(two)
    # 控制ID与age必须是这两个参数并且有值（可修改指定值）
    # if not ID or not age:
    #     return is_net(return_dict)
    # 对参数进行操作
    # return_dict['id']=id
    # return_dict['result']=get_to_data()
    return json.dumps(return_dict, ensure_ascii=False)


# 获取数据返回（获取数据方式自行修改）
def get_to_data():
    csv_file = csv.reader(open('data.csv', 'r'))
    data_ = []
    for line in csv_file:
        ID = line[0]
        url = line[1]
        result_str = {'id': ID, 'url': url}
        data_.append(result_str)
    return data_


if __name__ == "__main__":
    # port指定端口号
    app.run(port=2222, debug=True)
