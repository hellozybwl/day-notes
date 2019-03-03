import time
import logging
import os

root_path = os.getcwd() + "/../"

time_now = int(time.time())
time_local = time.localtime(time_now)
dt = time.strftime("%Y_%m_%d_%H_%M_%S",time_local)


log_file = root_path + "log/" + dt + ".log"


#日志文件测试
# debug 、info 、warning 、error 、critical
file = logging.FileHandler(filename=log_file, mode='a', encoding='utf-8')
fmt = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s", datefmt='%Y-%m-%d %H:%M:%S')
file.setFormatter(fmt)
logger = logging.Logger(name='测试日志', level=logging.DEBUG)
logger.addHandler(file)