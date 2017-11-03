from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
app.debug = True

conn = sqlite3.connect(r'./db/feedback.db')
c = conn.cursor()

@app.route('/')
def hello_world():
    return render_template('base.html')

@app.route('/feedback/')
def feedback():
    # categories = [(1, '产品质量'), (2, '客户服务'), (3, '购买支付')]
    sql = 'select rowid,categoryname from category'
    categories = c.execute(sql).fetchall()
    return render_template('post.html', categories=categories)

if __name__ == '__main__':
    app.run()