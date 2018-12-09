__author__ = 'Administrator'
# 数据库配置
db_host = '115.28.108.130'
db_port = 3306
db_user = 'test'
db_password = '123456'
db = 'api_test'
#配置路径
import os
config_path =os.path.abspath(__file__)
conf_path =os.path.dirname(config_path)
project_path = os.path.dirname(conf_path)

#project_path= os.path.rname(os.path.dirmame(os.path.dimame(os.path.abspath(__file__))))
#数据文件目录
#data_path = os.path.join(project_path,"data")
data_file = os.path.join(project_path,'data','data.xlsx')
#日志文件
log_file =os.path.join(project_path,'log','log.txt')
report_file= os.path.join(project_path,'report','report.html')



import logging

logging.basicConfig(level=logging.DEBUG,
                   format = "%(asctime)s %(levelname)s %(funcName)s [%(filename)s-%(lineno)d] %(message)s",
                   datefmt="%Y-%m-%d %H:%M:%S",
                   filename=log_file
                   )

smtp_server ='smtp.163.com'
smtp_user ='ivan-me@163.com'
smtp_password ='hanzhichao123'

receiver = 'superhin@126.com'
subject = '接口测试报告'
body = 'hi, all,\n附件中是接口测试报告,请查收.'

is_send_report = False
if __name__ == "__main__":
    #logging.info("hello,word")
    #logging.info("中文日志")

    print(os.path.abspath(__file__))
    print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))