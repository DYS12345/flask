from flask import Flask, render_template
from models.book import Book

app = Flask(__name__) # name是指定根路径
app.debug = True  #打开调试

@app.route('/')
def index():
	# 响应为web请求
	return render_template('index.html')

@app.route('/contact/')
def contact():
	return '联系我们'

@app.route('/books/')
def book_list():
	books = [
		Book('python flask', 59.00, 'dong', '人民邮电出版社'),
		Book('python selenium', 59.00, 'dong', '人民邮电出版社'),
		Book('python 爬虫', 59.00, 'dong', '人民邮电出版社'),
		Book('python 多线程', 59.00, 'dong', '人民邮电出版社'),
		Book('python 语言', 59.00, 'dong', '人民邮电出版社')
	]
	return render_template('book-list.html', books=books)

if __name__ == '__main__':
	app.run()