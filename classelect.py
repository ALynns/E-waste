from splinter.browser import Browser
from time import sleep
import traceback
import time,sys
import os

#需要python 3以上环境
#需要python安装splinter包 pip install splinter
#如果使用chrome浏览器需要chromedriver 版本对照https://blog.csdn.net/BinGISer/article/details/88559532 将其与.py文件放同一目录下

class selectCourse(object):
        #指定浏览器类型
        driver_name='chrome'
        executable_path=''
        #用户名 密码
        username = ""
        passwd = ""
        #cookies值自己找
        order = 0
        """网址"""
        #4m3登录URL
        login_url = "https://ids.tongji.edu.cn:8443/nidp/saml2/sso?id=1868&sid=0&option=credential&sid=0"
        #4m3主页URL
        initmy_url = "http://4m3.tongji.edu.cn/eams/home.action"
        #选课页面URL,先手动点击选课页面然后再拷贝过来,不同人选课页面可能不同
        elect_url=''
    
        def __init__(self):
            self.driver_name = 'chrome'
            self.executable_path = os.getcwd()+'/chromedriver'
            print("Welcome To Use The Tool")
        
        def login(self):
            self.driver.visit(self.initmy_url)
            #填充密码
            self.driver.fill("Ecom_User_ID",self.username)
            #sleep(1)
            self.driver.fill("Ecom_Password",self.passwd)
            #print("等待验证码，自行输入....")
            while True:
                if self.driver.url != self.initmy_url:
                    sleep(1)
                else :
                    break
        def start(self):
            self.driver = Browser(driver_name=self.driver_name,executable_path = self.executable_path)
            self.driver.driver.set_window_size(1400,1000)
            self.login()
            #sleep(1)
            while(True):
                self.driver.visit(self.initmy_url)
                self.driver.visit(self.elect_url)
                
                #课号，F12自己查
                self.driver.find_by_id("").click()
                #教师课号，F12自己查
                self.driver.find_by_id("").click()
                count=0
                while (True):
                    self.driver.find_by_id("savetable-btn").click()
                    sleep(2)
                    self.driver.find_by_id("cboxClose").click()
                    #选课间隔时间，不建议太短，否则会崩溃
                    sleep(3)
                    print("已抢%d次" %count)


    
if __name__=="__main__":
    course = selectCourse()
    course.start()