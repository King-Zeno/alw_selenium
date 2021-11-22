import time
from ddt import ddt, data, unpack
from time import sleep
import xlrd, unittest
import yaml
import selenium
import pytesseract
from PIL import Image
from selenium import webdriver
from demo1.image_verify import VerificationCode

def get_data(file_name):
    rows = []
    book = xlrd.open_workbook(file_name)
    sheet = book.sheet_by_index(0)
    for row_idx in range(1, sheet.nrows):
        rows.append(list(sheet.row_values(row_idx, 0, sheet.ncols)))
    return rows

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

    #登录商品库管理平台
    def test_alw_login(self):
        Browser = self.driver
        URL= "http://mms.test.anlewo.com:8377/"
        Browser.get(URL)
        Browser.maximize_window()
        image_str = VerificationCode.image_str

        element_name = Browser.find_element_by_xpath('/html/body/div/div/div[1]/form/div[1]/div/div/input')
        element_pswd = Browser.find_element_by_xpath('/html/body/div/div/div[1]/form/div[2]/div/div/input')
        element_name.send_keys('13800138000')
        element_pswd.send_keys('alw_2016')

        sleep(3)
        Browser.find_element_by_xpath('/html/body/div/div/div[1]/form/button').click()
        sleep(3)
        #111

    # def test_getdata(self):
    #     print(get_data('goods_data.xlsx'))

    @data(*get_data('goods_data.xlsx'))
    @unpack
    def test_add_goods(self, goods_classes, manage_class, release_class,goods_id,
                       sku_id, brand, conpany_version, alw_version, effect_product,
                       length, width, thickness, sku_goods_params, sale_box_rules, sale_rule,
                       purchase_box_rules, purchase_rule, goods_name, goods_class, if_sampling,
                       if_collection, if_sales_alone, if_recommend, if_is_parts, if_division_batch,
                       c_platform, b_platform, inside_platform, sample_platform, status, delivery_dates,
                       if_retail, min_buy_num, min_buy_unit, upload_time, move_time):
        pass

if __name__ == '__main__':
   pass