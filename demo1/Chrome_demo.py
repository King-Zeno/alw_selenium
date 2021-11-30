import time
import pytest
from time import sleep
import xlrd, unittest
import yaml
import selenium
from selenium import webdriver

def get_data(file_name):
    rows = []
    book = xlrd.open_workbook(file_name)
    sheet = book.sheet_by_index(1)
    for row_idx in range(1, sheet.nrows):
        rows.append(list(sheet.row_values(row_idx, 0, sheet.ncols)))
    print(rows)
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
        #111

    # def test_getdata(self):
    #     print(get_data('goods_data.xlsx'))
    value = get_data('goods_data.xlsx')
    @pytest.mark.parametrize('data', value)
    def test_add_goods(self, data):
        goods_classes = data[0]
        manage_class = data[1]
        release_class = data[2]
        goods_id = data[3]
        sku_id = data[4]
        brand = data[5]
        conpany_version = data[6]
        alw_version = data[7]
        effect_product = data[8]
        length = data[9]
        width = data[10]
        thickness = data[11]
        sku_goods_params = data[12]
        sale_box_rules = data[13]
        sale_rule = data[14]
        purchase_box_rules = data[15]
        purchase_rule = data[16]
        goods_name = data[17]
        goods_class = data[18]
        if_sampling = data[19]
        if_collection = data[20]
        if_sales_alone = data[21]
        if_recommend = data[22]
        if_is_parts = data[23]
        if_division_batch = data[24]
        c_platform = data[25]
        b_platform = data[26]
        inside_platform = data[27]
        sample_platform	 = data[28]
        status = data[29]
        delivery_dates = data[30]
        if_retail = data[31]
        min_buy_num	  = data[32]
        min_buy_unit = data[33]
        first_upload_time  = data[34]
        upload_time = data[35]
        move_time = data[36]

        # 登录商品库管理平台
        Browser = self.driver
        URL = "http://mms.test.anlewo.com:8377/"
        Browser.get(URL)
        Browser.maximize_window()

        element_name = Browser.find_element_by_xpath('/html/body/div/div/div[1]/form/div[1]/div/div/input')
        element_pswd = Browser.find_element_by_xpath('/html/body/div/div/div[1]/form/div[2]/div/div/input')
        element_name.send_keys('13800138000')
        element_pswd.send_keys('alw_2016')

        sleep(3)
        Browser.find_element_by_xpath('/html/body/div/div/div[1]/form/button').click()
        sleep(3)

        create_goods = Browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/div[2]/div[1]/div[2]/div[1]/div/div/button[1]/span')
        create_goods.click()
        if goods_classes == '普通商品':
            Browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/form/div[1]/div/div/div[1]/div/span').click()
            sleep(1)
            Browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/form/div[1]/div/div/div[2]/ul[2]/li[1]').click()
            sleep(1)
            if manage_class == '地砖':
                Browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/form/div[2]/div/div/div[1]/div[1]/input').click()
                sleep(1)
                Browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/form/div[2]/div/div/div[2]/div/span/ul/li[1]').click()
                sleep(1)
                Browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/form/div[2]/div/div/div[2]/div/span/span/ul/li[1]').click()
                sleep(1)
                element_tile = Browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/form/div[2]/div/div/div[2]/div/span/span/span/ul/li[1]')
                element_tile.click()
                sleep(1)
                if brand == '东鹏瓷砖':
                    Browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/form/div[3]/div/div/div[1]/div/span').click()
                    sleep(1)
                    Browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/form/div[3]/div/div/div[2]/ul[2]/li[31]').click()
                    sleep(1)
                    Browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[3]/div/button[2]').click()
                    sleep(3)

if __name__ == '__main__':
   pass

