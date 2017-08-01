from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
import json
import hashlib
import sqlite3

app = Flask(__name__)

ApiKey = 'A91CE25DECC7E6E8'
ApiSecret = '8639E817862EB929A993E30FA7846C4F'

table_name = 'wechat'
db_path = 'C:\\Users\\bobo1\\PycharmProjects\\WhatEat\\wechat.db'
# db_path = './wechat.db'


# 显示页面方便
@app.route('/index.html', methods=['GET'])
def show():
    return render_template('index.html')


@app.route('/get_data', methods=['POST'])
def ret_data():
    return jsonify(get_data())


def get_data():
    data = sqlite3.connect(db_path)
    cursor = data.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS ''' + table_name +
                   ''' (_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name text, 
                    eat_here INTEGER, 
                    eat_out INTEGER, 
                    area_1 INTEGER, 
                    area_2 INTEGER, 
                    area_3 INTEGER, 
                    area_4 INTEGER, 
                    id text);''')

    cursor.execute('''SELECT * FROM ''' + table_name + ''' WHERE id= ''' + repr(request.form.get('media_id')))
    list_tmp = []
    for item in cursor:
        list_tmp.append({'name': item[1], 'eat_here': item[2],
                         'eat_out': item[3], 'area_1': item[4],
                         'area_2': item[5], 'area_3': item[6],
                         'area_4': item[7], '_id': item[0]})
    cursor.close()
    return list_tmp


@app.route('/set_data', methods=['POST'])
def inset_data():
    data = sqlite3.connect(db_path)
    cursor = data.cursor()

    cursor.execute("INSERT INTO " + table_name + " VALUES (NULL,?,?,?,?,?,?,?,?)",
                   (request.form.get('name', ''), request.form.get('eat_here', 0),
                    request.form.get('eat_out', 0), request.form.get('area_1', 0),
                    request.form.get('area_2', 0), request.form.get('area_3', 0),
                    request.form.get('area_4', 0), request.form.get('id')))

    data.commit()
    cursor.close()
    return 'done'


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


# 用于调试 实际用index?type=config
@app.route('/config', methods=['GET'])
def config_page():
    return render_template('config.html')


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
    dic = request.args.to_dict()
    if calsign(dic) == dic.get('sign'):
        return render_template('config.html')
    else:
        return 'sign error'


def monitor():
    return request.args.get('echostr')


def trigger():
    return show()


def keyword():
    return jsonify({'errcode': 0, 'errmsg': 'OK'})


# 签名算法
def calsign(formdict):
    signstr = ''
    for key in sorted(list(formdict.keys())):
        if key == 'sign' or key == 'keyword' or key == 'type' or formdict[key] == '':
            continue
        signstr += key + '=' + str(formdict.get(key)) + '&'
    signstr += 'key=' + ApiSecret
    m = hashlib.md5()
    m.update(signstr.encode('utf-8'))
    signstr = m.hexdigest()
    return signstr.upper()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
