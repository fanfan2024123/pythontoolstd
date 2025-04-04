import os, webbrowser
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

print("提示输入的端口号必须为1-65535之间的数字")
port =int(input("设置端口号:"))
f=input("设置要共享的目录:")
os.chdir(f)  # 设置要共享的目录
webbrowser.open(f'http://localhost:{port}') #使用浏览器打开这个链接
TCPServer(('', port), SimpleHTTPRequestHandler).serve_forever() #启动服务