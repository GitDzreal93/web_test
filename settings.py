import os
import time

# 路径设置
BASE_DIR = os.path.dirname(os.path.abspath(__file__)).replace("\\","/")
CASE_DIR = os.path.join(BASE_DIR,'TestCase').replace("\\","/")
ELE_DIR = os.path.join(BASE_DIR,'EleMapping').replace("\\","/")
DATA_DIR = os.path.join(BASE_DIR,'DataConf').replace("\\","/")
REPORT_DIR = os.path.join(BASE_DIR,'Report').replace("\\","/")

#时间设置
NOW = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
DAY = time.strftime('%Y-%m-%d', time.localtime(time.time()))

