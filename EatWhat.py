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


#处理最基本的开启等相关
@app.route('/index', methods=['POST', 'GET'])
def base():
    re = None
    type = request.args.get('type')
    if type == 'open':
        re = open()
    elif type == 'close':
        re = close()
    elif type == 'config':
        re = config()
    elif type == 'monitor':
        re = monitor()
    elif type == 'trigger':
        re = trigger()
    elif type == 'keyword':
        re = keyword()
    else:
        re = 'service well'
    return re


# 显示页面
@app.route('/index.html')
def show():
    return render_template('index.html')


def open():
    if calsign(request.form) == request.form.get('sign'):
        return jsonify({'errcode': 0, 'is_config': 1})
    else:
        return jsonify({'errcode': 5004, 'errmsg': 'sign error'})


def close():
    if calsign(request.form) == request.form.get('sign'):
        return jsonify({'errcode': 0, 'errmsg': 'OK'})
    else:
        return jsonify({'errcode': 5004, 'errmsg': 'sign error'})


def config():
    return jsonify({'errcode': 0, 'errmis': 'OK'})


def monitor():
    return request.args.get('echostr')


def trigger():
    return web


def keyword():
    return jsonify({'errcode': 0, 'errmis': 'OK'})


# 签名算法
def calsign(formdict):
    signstr = ''
    d = json.loads(formdict.to_dict().keys().pop())
    for key in sorted(d.keys()):
        if key == 'sign' or key == 'keyword' or formdict[key] == '':
            continue
        signstr += key + '=' + d.get(key) + '&'
    signstr += 'key=' + ApiSecret
    m = hashlib.md5()
    m.update(signstr.encode('utf-8'))
    signstr = m.hexdigest()
    return signstr.upper()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
