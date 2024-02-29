'''
Author: 745719408@qq.com 745719408@qq.com
Date: 2024-02-29 14:34:29
LastEditors: 745719408@qq.com 745719408@qq.com
LastEditTime: 2024-02-29 14:37:40
FilePath: \FileDownloader\apprun.py
Description: 这是一个flask脚本写的文件下载器，主要用于一个地方从互联网下载文件，另外无法访问互联网的主机从这个脚本提供的服务去下载内网文件
'''
import os
from flask import Flask, send_from_directory, abort

app = Flask(__name__)

DOWNLOAD_DIRECTORY = os.environ.get('FLASK_DOWNLOAD_FOLDER', '/app')

@app.route('/download/<filename>')
def download_file(filename):
    if os.path.exists(os.path.join(DOWNLOAD_DIRECTORY, filename)):
        return send_from_directory(DOWNLOAD_DIRECTORY, filename, as_attachment=True)
    else:
        abort(404)

if __name__ == '__main__':
    app.run(host='0.0.0.0' ,port=5000,debug=True)