from mitmproxy import http
import re
import time
import queue
import threading
import zipfile
import os
# import json
import adbManager

# 定义文件路径、包名和文件名常量
filePath = "/home/jason/文档/软件设计/XiaoYuanKouSuan/"
PackageName = "replacePackage.zip"
fileName = "bao/"

# 定义延迟时间常量
delayTime = 5

# 定义需要拦截的URL模式列表
URLS_response = [
    r"leo\.fbcontent\.cn/bh5/leo-web-oral-pk/leo_web_oral_pk_.*\.zip",
    r"leo\.fbcontent\.cn/bh5/leo-web-oral-pk/exercise_.*\.js\?.*",
    r"xyks\.yuanfudao\.com/bh5/leo-web-oral-pk/exercise\.html\?.*",
    r"leo\.fbcontent\.cn/bh5/leo-web-oral-pk/leo_web_oral_pk_full_.*\.zip",
    r"leo\.fbcontent\.cn/bh5/leo-web-oral-pk/media/ready_go\..*\.mp3",
    r"xyks\.yuanfudao\.com/bh5/leo-web-oral-pk/result.html\?.*"
]


# 定义一个函数来拦截和处理特定的URL
def urlIntercept(url):
    """
    拦截并匹配给定的URL，返回匹配的URL模式索引。

    参数:
    - url (str): 需要拦截的URL。

    返回:
    - int: 匹配的URL模式索引，如果没有匹配则返回None。
    """
    for i in range(len(URLS_response)):
        if re.search(URLS_response[i], url):
            return i

# 定义一个函数来压缩指定文件夹中的所有文件
def zip_folder(folder_path, output_path):
    """
    压缩指定文件夹中的所有文件到一个ZIP文件中。

    参数:
    - folder_path (str): 要压缩的文件夹路径。
    - output_path (str): 输出的ZIP文件路径。
    """
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, folder_path))

# 定义一个ADB管理类
class adb_manager:
    def __init__(self):
        """
        初始化ADB管理器，设置自动点击答案的标志。
        """
        self._auto_click_answer_run = True

    def closeThread(self, function: str):
        """
        关闭指定的线程。

        参数:
        - function (str): 要关闭的线程名称。
        """
        match function:
            case "auto_click_answer":
                self._auto_click_answer_run = False
                print(self._auto_click_answer_run)

    def auto_click_answer(self):
        """
        自动点击答案，直到 `_auto_click_answer_run` 标志被设置为False。
        """
        self._auto_click_answer_run = True
        print("auto_click_answer")
        while self._auto_click_answer_run:
          time.sleep(0.01)
          adbManager.answerQuestion()

    def auto_click_continue(self):
        """
        自动点击继续按钮，包括多个步骤。
        """
        time.sleep(delayTime)
        adbManager.clickHappy()
        time.sleep(delayTime)
        adbManager.clickContinue_1()
        time.sleep(delayTime)
        adbManager.clickContinue_2()

# 定义一个响应处理器类
class ResponseHandler:
    def __init__(self):
        """
        初始化响应处理器。
        """
        pass

    def request(self, flow: http.HTTPFlow):
        """
        处理HTTP请求。

        参数:
        - flow (http.HTTPFlow): HTTP请求流。
        """
        pass

    def response(self, flow: http.HTTPFlow):
        """
        处理HTTP响应，根据URL模式进行不同的处理。

        参数:
        - flow (http.HTTPFlow): HTTP响应流。
        """
        url = flow.request.url
        url_num = urlIntercept(url)
        match url_num:
            case 0:
                # 处理zip文件
                flow.response.content = self.replaceZIP()
            case 1:
                # 处理js文件
                flow.response.text = self.replaceJS()
            case 2:
                # 处理html文件
                flow.response.text = self.replaceHTML(flow.response.text)
            case 3:
                # 处理zip文件
                flow.response.content = self.replaceZIP()
            case 4:
                # 开启连点器
                auto_click_answer_thread = threading.Thread(target=adb.auto_click_answer)
                auto_click_answer_thread.start()
                # pass
            case 5:
                # 关闭连点器并自动点击继续按键
                adb.closeThread("auto_click_answer")
                auto_click_conntinue_thread = threading.Thread(target=adb.auto_click_continue)
                auto_click_conntinue_thread.start()
                # pass

    def replaceZIP(self):
        """
        替换ZIP文件内容。

        返回:
        - bytes: 替换后的ZIP文件内容。
        """
        zip_folder(filePath + fileName, filePath + PackageName)
        with open(filePath + PackageName, "rb") as file:
            data = file.read()
        os.remove(filePath + PackageName)
        return data

    def replaceJS(self):
        """
        替换JavaScript文件内容。

        返回:
        - str: 替换后的JavaScript文件内容。
        """
        with open(filePath + fileName + "exercise.js", mode="r") as file:
            data = file.read()
        return data

    def replaceHTML(self, sourceData: str):
        """
        替换HTML文件内容，添加时间戳参数。

        参数:
        - sourceData (str): 原始HTML内容。

        返回:
        - str: 替换后的HTML内容。
        """
        pos = re.search(r"leo\.fbcontent\.cn/bh5/leo-web-oral-pk/exercise_.*\.js", sourceData).span()[1]
        list_data = list(sourceData)
        list_data.insert(pos, "?A=" + str(time.time()))
        return "".join(list_data)

    def replaceJSON(self):
        """
        替换JSON文件内容（当前未实现）。
        """
        pass

    def replaceCSS(self):
        """
        替换CSS文件内容（当前未实现）。
        """
        pass

# 创建ADB管理器实例
adb = adb_manager()

# 注册响应处理器
addons = [
    ResponseHandler()
]