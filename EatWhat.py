from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
import json
import hashlib

app = Flask(__name__)

ApiKey = 'A91CE25DECC7E6E8'
ApiSecret = '8639E817862EB929A993E30FA7846C4F'
web = 'http://120.77.42.60:5000/index.html'


# 处理最基本的开启等相关
@app.route('/index', methods=['POST', 'GET'])
def base():
    re = None
    get_type = request.args.get('type')
    if get_type == 'open':
        re = open()
    elif get_type == 'close':
        re = close()
    elif get_type == 'config':
        re = config()
    elif get_type == 'monitor':
        re = monitor()
    elif get_type == 'trigger':
        re = trigger()
    elif get_type == 'keyword':
        re = keyword()
    else:
        re = 'service well'
    return re


# 显示页面
@app.route('/index.html')
def show():
    return render_template('index.html')


def open():
    dic = json.loads(list(request.form.to_dict().keys()).pop())
    if calsign(dic) == dic.get('sign'):
        return jsonify({'errcode': 0, 'is_config': 1})
    else:
        return jsonify({'errcode': 5004, 'errmsg': 'sign error'})


def close():
    dic = json.loads(list(request.form.to_dict().keys()).pop())
    if calsign(dic) == dic.get('sign'):
        return jsonify({'errcode': 0, 'errmsg': 'OK'})
    else:
        return jsonify({'errcode': 5004, 'errmsg': 'sign error'})


def config():
    return jsonify({'errcode': 0, 'errmis': 'OK'})


def monitor():
    return request.args.get('echostr')


def trigger():
    return render_template('index.html')


def keyword():
    return jsonify({'errcode': 0, 'errmis': 'OK'})


# 签名算法
def calsign(formdict):
    signstr = ''
    for key in sorted(list(formdict.keys())):
        if key == 'sign' or key == 'keyword' or formdict[key] == '':
            continue
        signstr += key + '=' + str(formdict.get(key)) + '&'
    signstr += 'key=' + ApiSecret
    m = hashlib.md5()
    m.update(signstr.encode('utf-8'))
    signstr = m.hexdigest()
    return signstr.upper()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
