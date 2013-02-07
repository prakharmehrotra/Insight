#!/usr/bin/env python

import os

from flask import Flask
from flask import url_for
from flask import render_template
from flask import jsonify
from flask import url_for
import MySQLdb



# MySQL connection variables
host = 'localhost'
user = 'root'
passwd = ''
db = 'NewsFeed'

def connect_db(host, user, passwd, db):
    try:
        return MySQLdb.connect(host, user, passwd, db)
    except MySQLdb.Error, e:
        sys.stderr.write("[ERROR]%d: %s\n" %(e.args[0], e.args[1]))
        return False


# Connecting with database
database = connect_db(host, user, passwd, db)
cur = database.cursor()



app = Flask(__name__)


@app.route('/')
def index():
    keyword = []
    cur.execute('USE NewsFeed')
    cur.execute('SELECT * FROM FILTERED_GRAMS Where Id>=1000 AND Id <10000')
    data = cur.fetchall()
    nrows = int(cur.rowcount)
    for i in range(0, 5):
        keyword.append((eval(data[i][1])[0] + ' ' + eval(data[i][1])[1]).title())
    print keyword
    return render_template('News_Visual.html', key1=keyword[0], key2 = keyword[1], key3 = keyword[2], key4 = keyword[3], key5 = keyword[4])


@app.route('/Advanced')
def anim():
    return render_template('advanced.html')

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    #app.run(host='192.168.1.33', port=5000)
    app.run(host='0.0.0.0', port=5000)
