from time import sleep
from poium import Page, Element, Elements
from poium import Browser
from selenium import webdriver

# page层定义
class loginPage(Page):
    mobile_number = Element(xpath="/html/body/div/div/div[1]/form/div[1]/div/div/input", describe="手机号码")
    password = Element(xpath="/html/body/div/div/div[1]/form/div[2]/div/div/input", describe="密码")
    login_button = Element(xpath='/html/body/div/div/div[1]/form/button', describe="登录按钮")
    #results = Elements(xpath="//div/h3/a", describe="搜索结果")
    create_button = Element(xpath="//button/span[text()='新建商品']", describe="登录按钮")
    good_classes = Element(xpath="/html/body/div[2]/div[2]/div/div/div[2]/form/div[1]/div/div/div[1]/div/span", describe="商品大类")
    manage_classes = Element(xpath="/html/body/div[2]/div[2]/div/div/div[2]/form/div[2]/div/div/div[1]/div[1]/input", describe="管理品类")
    brand = Element(xpath="/html/body/div[2]/div[2]/div/div/div[2]/form/div[3]/div/div/div[1]/div/span", describe="品牌")
    cancel_button = Element(xpath="/html/body/div[3]/div[2]/div/div/div[3]/div/button[1]/span", describe="取消按钮")
    nextstep_button = Element(xpath="/html/body/div[2]/div[2]/div/div/div[3]/div/button[2]", describe="下一步按钮")
    normal_goods = Element(xpath="/html/body/div[2]/div[2]/div/div/div[2]/form/div[1]/div/div/div[2]/ul[2]/li[1]", describe="普通商品")
    goods_parts = Element(xpath="/html/body/div[2]/div[2]/div/div/div[2]/form/div[1]/div/div/div[2]/ul[2]/li[2]", describe="商品部件")
    goods_element = Element(xpath="/html/body/div[2]/div[2]/div/div/div[2]/form/div[1]/div/div/div[2]/ul[2]/li[3]", describe="商品组件")
    goods_sale_property = Element(xpath="/html/body/div[2]/div[2]/div/div/div[2]/form/div[1]/div/div/div[2]/ul[2]/li[3]", describe="销售与施工道具")
    build_material = Element(xpath="//li/span[text()='建材']", describe="建材")
    china_tiles = Element(xpath="/html/body/div[2]/div[2]/div/div/div[2]/form/div[2]/div/div/div[2]/div/span/span/ul/li[1]", describe="瓷砖")
    ground_tiles = Element(xpath="/html/body/div[2]/div[2]/div/div/div[2]/form/div[2]/div/div/div[2]/div/span/span/span/ul/li[1]", describe="地砖")

dr = webdriver.Chrome(r'D:\Work\QA\selenium\webdriver\chromedriver.exe')
login = loginPage(dr)
login.get("http://mms.test.anlewo.com:8377/")
login.mobile_number.send_keys("13800138000")
login.password.send_keys("alw_2016")
login.login_button.click()
sleep(2)
login.create_button.click()
login.good_classes.click()
login.normal_goods.click()
login.manage_classes.click()

login.nextstep_button.click()
sleep(2)

dr.close()