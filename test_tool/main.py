import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QScrollArea, QLabel, QScrollBar, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt
from main_ui import *
import requests
import traceback
import json
import time


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.label = QLabel(self) 
        self.setupUi(self)
        self.init_ui()
        self.scroll_area = QScrollArea(self)                   
        self.scroll_area.setWidget(self.label)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        #self.scrollbar = QScrollBar(Qt.Horizontal, self)       # 3
        #self.scrollbar.setMaximum(self.scroll_area.horizontalScrollBar().maximum())


    def init_ui(self):
        self.pushButton.clicked.connect(self.buttonClicked1)
        self.pushButton_2.clicked.connect(self.buttonClicked2)

    def buttonClicked1(self):
        server_url = self.lineEdit.text().strip()
        port  = self.lineEdit_2.text().strip()
        interface_url =self.lineEdit_3.text().strip()
        http_method = self.comboBox.currentText().strip()
        headers = self.textEdit.toPlainText().strip()
        test_data = self.textEdit_2.toPlainText().strip()
        response,response_time = test_interface(server_url, interface_url, port, http_method, headers, test_data)
        self.response =response
        self.response_time = response_time*1000
        self.textEdit_3.setPlainText(response.strip())
        self.label_10.setText(str(self.response_time)+" ms")
        #self.textEdit_3.setText(response.strip())#会有网页渲染效果，但是速度超级慢，会卡死，所以使用setPlainText

    def buttonClicked2(self):
        server_url = self.lineEdit.text().strip()
        port = self.lineEdit_2.text().strip()
        interface_url = self.lineEdit_3.text().strip()
        http_method = self.comboBox.currentText().strip()
        headers = self.textEdit.toPlainText().strip()
        test_data = self.textEdit_2.toPlainText().strip()
        response = self.response
        response_time = self.response_time

        save_test_result(server_url, interface_url, port, http_method, headers, test_data, response,response_time)
        print("保存数据成功！")


def test_interface(server_url, interface_url, port, http_method, headers, test_data):
    test_url = server_url + ":" + port + interface_url
    print("服务器url:", server_url)
    print("服务器端口:", port)
    print("接口url 地址：", interface_url)
    print("http 协议方法：", http_method)
    print("请求的头信息:", headers)
    print("接口请求数据：", test_data)

    try:
        if headers.strip()!="":#如果头信息不为空，则转换为字典
            headers = json.loads(headers)#header必须是字典类型才可以
        else:
            headers ={}

        if "post" in http_method.lower():
            start_time = time.time()
            response = requests.post(test_url, data=test_data,headers=headers)
            end_time = time.time()
            response_time = round(end_time - start_time,2)
            print("接口响应数据：", response.text)
            print("接口响应时间：%s ms" % (response_time*1000))
            print("-"*50+"\n")
            return response.text,response_time

        if "get" in http_method.lower():
            start_time = time.time()
            response = requests.get(test_url, headers=headers)
            end_time = time.time()
            response_time = round(end_time - start_time, 2)
            print("接口响应数据：", response.text)
            print("接口响应时间：%s ms" % (response_time*1000))
            print("-"*50+"\n")
            return response.text,response_time

        if "put" in http_method.lower():
            start_time = time.time()
            response = requests.put(test_url, headers=headers)
            end_time = time.time()
            response_time = round(end_time - start_time, 2)
            print("接口响应数据：", response.text)
            print("接口响应时间：%s ms" % (response_time*1000))
            print("-"*50+"\n")
            return response.text,response_time



    except Exception as e:
        print(e)
        traceback.print_exc()
        return str(e),0

def save_test_result(server_url, interface_url, port, http_method, headers, test_data,response,response_time):
    with open("test_result.txt","a",encoding="utf-8") as fp:
        test_url = server_url + ":" + port + interface_url
        fp.write("接口测试的时间：%s \n" %time.strftime("%Y-%m-%d %H:%M:%S"))
        fp.write("接口 url 地址：%s\n" %test_url )
        fp.write("接口 http 请求方法：%s\n" %  http_method)
        fp.write("接口请求的 header 信息：%s\n" % headers)
        fp.write("接口请求的测试数据：%s\n" % test_data)
        fp.write("接口响应结果：%s\n" % response)
        fp.write("接口响应时间：%s ms\n" % response_time)

        fp.write("-"*50+"\n")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())



# response = test_interface("http://124.223.167.147","/register/","8080","post",{'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36','Content-Type': 'application/json'},'{"username":"l11ily","password":"l123224567","email":"lily@qq.com"}')

#print(response)
