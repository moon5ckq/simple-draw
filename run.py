#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 mlckq <moon5ckq@gmail.com>
#
# Distributed under terms of the MIT license.

import sys, random
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
db.init_app(app)
db.app = app

'''
class Test(db.Model):
  id = db.Column(db.Integer, primary_key = True)

  def __repr__(self):
    return '<test>'
'''

# const
path = 'data/raw'

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/random/<int:m>', methods=['POST','GET'])
def random_num(m):
    dis = set()
    with open(path, 'r') as f:
        for line in f:
            for t in line.split(','):
                if t.find('-') != -1:
                    dis = dis | set(range(int(t.split('-')[0]), int(t.split('-')[1]) + 1))
                else:
                    dis.add(int(t))
    ret = None
    try:
        ret = random.choice(list(set(range(1, m+1)) - dis))
        dis.add(ret)
    except:
        ret = -1

    with open(path, 'w') as f:
        f.write( ','.join(map(str, list(dis))) )

    return str(ret)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=23333, debug=True)
