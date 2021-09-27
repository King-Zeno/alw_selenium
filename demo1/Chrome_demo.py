import time
from time import sleep
import yaml
import selenium
import pytesseract
from PIL import Image
from selenium import webdriver
from demo1.image_verify import VerificationCode

class Test_selenium():
    def setup(self):
        chrome_driver = r'D:\Work\QA\selenium\webdriver\chromedriver.exe'
        options = webdriver.ChromeOptions()
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option("excludeSwitches", ['enable-automation'])
        self.driver = webdriver.Chrome(options=options,executable_path=chrome_driver)
        self.find_element = self.driver.find_element_by_css_selector
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    #登录门店管理平台
    def test_alw_login(self):
        Browser = self.driver
        URL= "http://store.test.alwooo.com:8338"
        Browser.get(URL)
        Browser.maximize_window()
        image_str = VerificationCode.image_str

        element_name = Browser.find_element_by_id('usertable-mobile')
        element_pswd = Browser.find_element_by_id('usertable-password')
        element_verf = Browser.find_element_by_id('usertable-verifycode')
        Browser.find_element_by_id('checkbox').click()
        verify_code1 = image_str(VerificationCode(), self.get_pictures())
        element_name.send_keys('15898765432')
        element_pswd.send_keys('alw_2016')
        element_verf.send_keys(verify_code1)

        sleep(3)
        Browser.find_element_by_xpath('//*[@id="login"]/div[4]/div[2]/button').click()
        sleep(3)
        #111

    def get_pictures(self):
        self.driver.save_screenshot('pictures.png')  # 全屏截图
        page_snap_obj = Image.open('pictures.png')
        img = self.find_element('#usertable-verifycode-image')  # 验证码元素位置
        time.sleep(1)
        location = img.location
        size = img.size  # 获取验证码的大小参数
        left = location['x']
        top = location['y']
        right = left + size['width']
        bottom = top + size['height']
        image_obj = page_snap_obj.crop((left, top, right, bottom))  # 按照验证码的长宽，切割验证码
        #image_obj.show()  # 打开切割后的完整验证码
        #self.driver.close()  # 处理完验证码后关闭浏览器
        return image_obj

class login_collect():

    def test_alw_login(self):
        Browser = self.driver
        URL= "http://store.test.alwooo.com:8338"
        Browser.get(URL)
        Browser.maximize_window()
        image_str = VerificationCode.image_str

        element_name = Browser.find_element_by_id('usertable-mobile')
        element_pswd = Browser.find_element_by_id('usertable-password')
        element_verf = Browser.find_element_by_id('usertable-verifycode')
        Browser.find_element_by_id('checkbox').click()
        verify_code1 = image_str(VerificationCode(), self.get_pictures())
        element_name.send_keys('15898765432')
        element_pswd.send_keys('alw_2016')
        element_verf.send_keys(verify_code1)

        sleep(3)
        Browser.find_element_by_xpath('//*[@id="login"]/div[4]/div[2]/button').click()
        sleep(3)
    #需要门店先登录
    def test_ipad_login(self):
        Browser = self.driver
        URL= "http://store.test.alwooo.com:8338/Dev/index/index"
        Browser.get(URL)
        Browser.maximize_window()
        #image_str = VerificationCode.image_str

        element_name = Browser.find_element_by_id('usertable-mobile')
        element_pswd = Browser.find_element_by_id('usertable-password')
        element_verf = Browser.find_element_by_id('usertable-verifycode')
        Browser.find_element_by_id('checkbox').click()
        #verify_code1 = image_str(VerificationCode(), self.get_pictures())
        element_name.send_keys('15898765432')
        element_pswd.send_keys('alw_2016')
        #element_verf.send_keys(verify_code1)

        sleep(3)
        Browser.find_element_by_xpath('//*[@id="login"]/div[4]/div[2]/button').click()
        sleep(3)