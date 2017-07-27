from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
import hashlib

app = Flask(__name__)

ApiKey = 'A91CE25DECC7E6E8'
ApiSecret = '8639E817862EB929A993E30FA7846C4F'


#处理最基本的开启等相关
@app.route('/index', methods=['POST', 'GET'])
def base():
    type = request.args.get('type')
    if type == 'open':
        open()
    elif type == 'close':
        close()
    elif type == 'config':
        config()
    elif type == 'monitor':
        monitor()
    elif type == 'trigger':
        trigger()
    elif type == 'keyword':
        keyword()


def open():
    if calsign(request.form) == request.form.get('sign'):
        return jsonify({'errcode': 0, 'is_config': 1})
    else:
        return jsonify({'errcode': 5004, 'errmsg': 'sign error'})


def close():
    if calsign(request.form) == request.form.get('sign'):
        return jsonify({'errcode': 0, 'errmis': 'OK'})
    else:
        return jsonify({'errcode': 5004, 'errmsg': 'sign error'})


def config():
    return jsonify({'errcode': 0, 'errmis': 'OK'})


def monitor():
    return request.args.get('echostr')


def trigger():
    return render_template('index.html')


def keyword():
    return


#签名算法
def calsign(formdict):
    signstr = ''
    keys = list(formdict.iterkeys).sort()
    for key in keys:
        if key == 'sign' or key == 'keyword':
            continue
        signstr += key + '=' + formdict[key] + '&'
    signstr += 'key=' + ApiSecret
    m = hashlib.md5()
    m.update(signstr)
    signstr = m.hexdigest()
    return signstr.upper()


if __name__ == '__main__':
    app.run()
