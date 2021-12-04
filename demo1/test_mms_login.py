from time import sleep
from poium import Page, Element, Elements
from poium import Browser
from selenium import webdriver

# page层定义
class loginPage(Page):
    #登录页
    mobile_number = Element(xpath="/html/body/div/div/div[1]/form/div[1]/div/div/input", describe="手机号码")
    password = Element(xpath="/html/body/div/div/div[1]/form/div[2]/div/div/input", describe="密码")
    login_button = Element(xpath='/html/body/div/div/div[1]/form/button', describe="登录按钮")
    #results = Elements(xpath="//div/h3/a", describe="搜索结果")
    #商品管理页
    create_button = Element(xpath="//button/span[text()='新建商品']", describe="登录按钮")
    good_classes = Element(xpath="/html/body/div[2]/div[2]/div/div/div[2]/form/div[1]/div/div/div[1]/div/span", describe="商品大类")
    manage_classes = Element(xpath="/html/body/div[2]/div[2]/div/div/div[2]/form/div[2]/div/div/div[1]/div[1]/input", describe="管理品类")
    brand = Element(xpath="/html/body/div[2]/div[2]/div/div/div[2]/form/div[3]/div/div/div[1]/div/span", describe="品牌")
    cancel_button = Element(xpath="/html/body/div[3]/div[2]/div/div/div[3]/div/button[1]/span", describe="取消按钮")
    nextstep_button1 = Element(xpath="/html/body/div[2]/div[2]/div/div/div[3]/div/button[2]", describe="下一步按钮")
    normal_goods = Element(xpath="/html/body/div[2]/div[2]/div/div/div[2]/form/div[1]/div/div/div[2]/ul[2]/li[1]", describe="普通商品")
    goods_parts = Element(xpath="/html/body/div[2]/div[2]/div/div/div[2]/form/div[1]/div/div/div[2]/ul[2]/li[2]", describe="商品部件")
    goods_element = Element(xpath="/html/body/div[2]/div[2]/div/div/div[2]/form/div[1]/div/div/div[2]/ul[2]/li[3]", describe="商品组件")
    goods_sale_property = Element(xpath="/html/body/div[2]/div[2]/div/div/div[2]/form/div[1]/div/div/div[2]/ul[2]/li[3]", describe="销售与施工道具")
    build_material = Element(xpath="/html/body/div[2]/div[2]/div/div/div[2]/form/div[2]/div/div/div[2]/div/span/ul/li[1]", describe="建材")
    china_tiles = Element(xpath="/html/body/div[2]/div[2]/div/div/div[2]/form/div[2]/div/div/div[2]/div/span/span/ul/li[1]", describe="瓷砖")
    ground_tiles = Element(xpath="/html/body/div[2]/div[2]/div/div/div[2]/form/div[2]/div/div/div[2]/div/span/span/span/ul/li[1]", describe="地砖")
    dongpengcizhuan = Element(xpath="/html/body/div[2]/div[2]/div/div/div[2]/form/div[3]/div/div/div[2]/ul[2]/li[31]", describe="东鹏瓷砖")
    #新建商品页
    collection_y = Element(xpath="/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[1]/form/div/div[4]/div/div/div/label[2]", describe="可作为配件")
    collection_n = Element(xpath="/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[1]/form/div/div[4]/div/div/div/label[1]", describe="不可作为配件")
    sales_alone_y = Element(xpath="/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[1]/form/div/div[5]/div/div/div/label[2]", describe="可单独销售")
    sales_alone_n = Element(xpath="/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[1]/form/div/div[5]/div/div/div/label[1]", describe="不可单独销售")
    alw_version = Element(xpath="/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[1]/form/div/div[7]/div/div/div/input", describe="安乐窝型号")
    conpany_version = Element(xpath="/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[1]/form/div/div[8]/div/div/div/input", describe="厂家型号")
    Commodity_units = Element(xpath="/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[1]/form/div/div[9]/div/div/div/div[1]/div/span", describe="商品单位")
    division_batch_y = Element(xpath="/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[1]/form/div/div[10]/div/div/div/label[2]", describe="区分批次")
    division_batch_n = Element(xpath="/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[1]/form/div/div[10]/div/div/div/label[1]", describe="不区分批次")
    length = Element(xpath="/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[1]/form/div/div[11]/div/div/div[1]/div/div/div[2]/input", describe="长")
    width = Element(xpath="/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[1]/form/div/div[11]/div/div/div[2]/div/div/div[2]/input", describe="宽")
    sale_box_rules_y = Element(xpath="/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[1]/form/div/div[12]/div/div/div[1]/label[2]", describe="有销售包装规格")
    sale_box_rules_n = Element(xpath="/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[1]/form/div/div[12]/div/div/div[1]/label[1]", describe="无销售包装规格")
    sale_box_rules_num = Element(xpath="/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[1]/form/div/div[12]/div/div/div[2]/div[2]/input", describe="有销售包装规格数")
    sale_box_rules_1 = Element(xpath="/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[1]/form/div/div[12]/div/div/div[3]/div[1]/div/span", describe="有销售包装规格单位1")
    sale_box_rules_2 = Element(xpath="/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[1]/form/div/div[12]/div/div/div[4]/div[1]/div/span", describe="有销售包装规格单位2")
    purchase_box_rules_y = Element(xpath="/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[1]/form/div/div[13]/div/div/div[1]/label[2]", describe="有采购包装规格")
    purchase_box_rules_n = Element(xpath="/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[1]/form/div/div[13]/div/div/div[1]/label[1]", describe="无采购包装规格")
    purchase_box_rules_num = Element(xpath="/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[1]/form/div/div[13]/div/div/div[2]/div[2]/input", describe="有采购包装规格数")
    purchase_box_rules_1 = Element(xpath="/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[1]/form/div/div[13]/div/div/div[3]/div[1]/div/span", describe="有采购包装规格单位1")
    purchase_box_rules_2 = Element(xpath="/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[1]/form/div/div[13]/div/div/div[4]/div[1]/div/span", describe="有采购包装规格单位2")
    package_weight = Element(xpath="/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[1]/form/div/div[14]/div/div/div/div[2]/input", describe="包装重量")
    package_volume = Element(xpath="/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[1]/form/div/div[15]/div/div/div/div[2]/input", describe="包装体积")
    goods_image = Element(xpath="/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[1]/form/div/div[16]/div/div/div/div/div/div/div", describe="商品大图")
    style1 = Element(xpath="/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[1]/form/div/div[17]/div/div/div/div/label[1]/span[2]", describe="北欧风格")
    stand_goods = Element(xpath="/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[1]/form/div/div[18]/div/div/div/label[1]", describe="标准品")
    customer_goods = Element(xpath="/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div[1]/div/div[1]/form/div/div[18]/div/div/div/label[2]", describe="定制品")
    nextstep_button2 = Element(xpath="/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/button[2]/span", describe="下一步按钮")
    save_button = Element(xpath="/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/button[3]", describe="保存按钮")
    cancel_button2 = Element(xpath="/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/button[5]", describe="取消按钮")





dr = webdriver.Chrome(r'D:\Work\QA\selenium\webdriver\chromedriver.exe')
dr.maximize_window()
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
login.build_material.click()
login.china_tiles.click()
login.ground_tiles.click()
login.brand.click()
login.dongpengcizhuan.click()
login.nextstep_button1.click()
sleep(2)

dr.close()