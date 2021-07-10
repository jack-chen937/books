from flask import Flask, jsonify
from books import Book
# 创建app应用,__name__是python预定义变量，被设置为使用本模块.
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
"""
返回前端格式
{
  rescode:1
  data:
  message:
}
"""


@app.route('/')
def index():
    book = Book()
    arr = book.get_data()
    return jsonify(arr)


if __name__ == '__main__':
    app.run()
