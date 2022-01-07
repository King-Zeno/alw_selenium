from time import sleep
from poium import Page, Element, Elements
from poium import Browser
import xlrd, pytest, xlwt
from selenium import webdriver

def get_data(file_name):
    rows = []
    book = xlrd.open_workbook(file_name)
    sheet = book.sheet_by_index(2)
    for row_idx in range(1, sheet.nrows):
        rows.append(list(sheet.row_values(row_idx, 0, sheet.ncols)))
    #print(rows)
    return rows

def write_data(num, falure_id):
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('sheet')
    worksheet.write(0, num, label=falure_id)
    workbook.save('Excel_Workbook.xls')

falure_id=[]
spuid_list = []

# page层定义
class loginPage(Page):
    #登录页
    mobile_number = Element(xpath="/html/body/div/div/div[2]/div[1]/div/form/div[1]/div/div/input", describe="手机号码")
    password = Element(xpath="/html/body/div/div/div[2]/div[1]/div/form/div[2]/div/div/input", describe="密码")
    login_button = Element(xpath="/html/body/div/div/div[2]/div[1]/div/form/div[3]/div/button", describe="登录按钮")
    brand_manager = Element(xpath="/html/body/div/div[1]/div/div/div[2]/ul/a[2]", describe="品牌管理")
    basic_manager = Element(xpath="/html/body/div/div[1]/div/div/div[2]/ul/a[3]", describe="基础管理")
    goods_manager = Element(xpath="/html/body/div/div[1]/div/div/div[2]/ul/a[4]", describe="商品管理")
    price_manager = Element(xpath="/html/body/div/div[1]/div/div/div[2]/ul/a[5]", describe="价格管理")
    brand_manager_next = Element(xpath="/html/body/div/div[1]/div[2]/div/ul/a[1]", describe="品牌管理1")
    contract_manager = Element(xpath="/html/body/div/div[1]/div[2]/div/ul/a[2]", describe="合同管理")
    format_manager = Element(xpath="/html/body/div/div[1]/div[2]/div/ul/a[3]", describe="版式管理")
    create_brand = Element(link_text="创建品牌", describe="创建品牌")
    goods_manager_next = Element(xpath="/html/body/div[1]/div[1]/div[2]/div/ul/a[1]", describe="商品管理1")
    select_search_text1 = Element(xpath="/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[2]/form/div/div[1]/div/div/div/div/div/div/div[1]/div/span", describe="商品管理选择搜索字段")
    search_alw_sn1 = Element(xpath="/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[2]/form/div/div[1]/div/div/div/div/div/div/div[2]/ul[2]/li[3]", describe="搜索安乐窝型号")
    search_spuid1 = Element(xpath="/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[2]/form/div/div[1]/div/div/div/div/div/div/div[2]/ul[2]/li[1]", describe="搜索spuid")
    search_skuid1 = Element(xpath="/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[2]/form/div/div[1]/div/div/div/div/div/div/div[2]/ul[2]/li[2]", describe="搜索skuid")
    search_input1 = Element(xpath="/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[2]/form/div/div[1]/div/div/div/div/input", describe="搜索输入文字")
    goods_search_button1 = Element(xpath="/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[2]/form/div/div[4]/button[1]/span", describe="搜索按钮")
    goods_resetting_button1 = Element(xpath="/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[2]/form/div/div[4]/button[2]/span", describe="重置按钮")
    goods_detail_button = Element(xpath="/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[3]/div[1]/div/div[1]/div[2]/table/tbody/tr/td[7]/div/a/span", describe="商品编辑按钮")
    #goods_detail_button = Element(link_text="编辑")
    basic_info = Element(xpath="/html/body/div[1]/div[2]/div[2]/div[1]/div/div[1]/div[1]/ul/li[1]", describe="基本信息")

    spec_property_list = Elements(xpath="/html/body/div[1]/div[2]/div[2]/div[1]/div/div[1]/div[1]/ul/li[2]", describe="规格属性")
    spec_property = Element(xpath="/html/body/div[1]/div[2]/div[2]/div[1]/div/div[1]/div[1]/ul/li[2]", describe="规格属性")

    company_version = Element(xpath="/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/table/tbody/tr/td[3]/div/div/div/textarea", describe="厂家型号")
    sale_box_rules = Element(xpath="/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/table/tbody/tr/td[4]/div/div/span/div/div[2]/input", describe="销售箱规")
    purchase_box_rules = Element(xpath="/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/table/tbody/tr/td[5]/div/div/span/div/div[2]/input", describe="采购箱规")
    length_input = Element(xpath="/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[1]/form/div/div[7]/div/div/div[1]/div/div/div[2]/input", describe="尺寸长")
    width_input = Element(xpath="/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[1]/form/div/div[7]/div/div/div[2]/div/div/div[2]/input", describe="尺寸宽")
    #customization_info = Element(xpath="/html/body/div[1]/div[2]/div[2]/div[1]/div/div[1]/div[1]/ul/li[3]", describe="定制信息")
    customization_info = Element(link_text="定制信息")
    submit_price_button=Element(xpath="/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/button[3]/span", describe="提交至发布按钮")

    brand_name = Element(xpath="/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[1]/form/div/div[3]/div/div/div/div/div/div[1]/div/span", describe="品牌名称")
    measurement_units = Element(xpath="/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[1]/form/div/div[4]/div/div/div/div/div/div[1]/div/span", describe="计量单位")
    alw_sn = Element(xpath="/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[1]/form/div/div[5]/div/div/div/div/div/input", describe="安乐窝型号")
    release_goods = Element(xpath="/html/body/div[1]/div[1]/div[2]/div/ul/a[2]", describe="发布商品")
    select_search_text2 = Element(xpath="/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[1]/form/div/div[1]/div/div/div/div/div/div/div[1]/div/span", describe="发布商品选择搜索框")
    search_skuid2 = Element(xpath="/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[1]/form/div/div[1]/div/div/div/div/div/div/div[2]/ul[2]/li[1]", describe="skuid")
    search_spuid2 = Element(xpath="/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[1]/form/div/div[1]/div/div/div/div/div/div/div[2]/ul[2]/li[2]", describe="spuid")
    search_alw_sn2 = Element(xpath="/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[1]/form/div/div[1]/div/div/div/div/div/div/div[2]/ul[2]/li[3]", describe="安乐窝型号")
    search_input2 = Element(xpath="/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[1]/form/div/div[1]/div/div/div/div/input", describe="搜索输入文字")
    goods_search_button2 = Element(xpath="/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[1]/form/div/div[4]/button[1]/span", describe="搜索按钮")
    goods_resetting_button2 = Element(xpath="/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[1]/form/div/div[4]/button[2]/span", describe="重置按钮")
    basic_info2 = Element(link_text="基本信息")
    goods_images = Element(link_text="商品图片")
    accessories_info = Element(link_text="配件信息")
    sub_goods_info = Element(link_text="子件信息")
    stone_info = Element(link_text="石基信息")
    recommend_goods = Element(link_text="推荐商品")
    soft_goods = Element(link_text="软装商品")
    #brand_name = Element(xpath="", describe="")
    #brand_name = Element(xpath="", describe="")


class Test_compare_data():
    def setup(self):
        option=webdriver.ChromeOptions()
        #option.add_argument('headless')
        #self.dr = webdriver.Chrome(r'D:\Work\QA\selenium\webdriver\chromedriver.exe', chrome_options=option)

        self.dr = webdriver.Chrome(r'D:\Work\QA\selenium\webdriver\chromedriver.exe')
        self.dr.maximize_window()
        self.search = loginPage(self.dr)
        self.search.open("http://amp.test.alwooo.com:8497/")
        self.search.mobile_number.send_keys("15575540001")
        self.search.password.send_keys("123456")
        self.search.login_button.click()
        sleep(1)

    def teardown(self):
        #write_data(0, falure_id)
        # print(falure_id)
        # print(spuid_list)
        self.dr.close()

    value = get_data('goods_data.xlsx')
    @pytest.mark.parametrize('data', value)
    def test_compare(self, data):
        goods_classes = data[0]
        spuid = data[3]
        skuid = data[4]
        company_version = data[6]
        sale_box_rules = data[13]
        purchase_box_rules = data[15]
        compare_data = self.search
        compare_data.goods_manager.click()
        compare_data.goods_manager_next.click()
        compare_data.select_search_text1.click()
        compare_data.search_spuid1.click()
        compare_data.search_input1.send_keys(spuid)
        compare_data.goods_search_button1.click()
        sleep(1)
        compare_data.goods_detail_button.click()  # 进入商品详情
        sleep(1)
        compare_data.width_input.send_keys(100)
        compare_data.length_input.send_keys(100)

        spec_property_list = compare_data.spec_property_list

        if(spec_property_list.__sizeof__() > 0):
            spec_property = compare_data.spec_property
            spec_property.click()
            company_version_get = compare_data.company_version.get_attribute("value")
            sale_box_rules_get = compare_data.sale_box_rules.get_attribute("value")
            purchase_box_rules_get = compare_data.purchase_box_rules.get_attribute("value")

            if company_version_get == '' or sale_box_rules_get == '' or purchase_box_rules_get == '':
                falure_id.append(spuid)
        # print(float(search.sale_box_rules.get_attribute("value")))
            else:
                assert company_version_get == str(company_version)
                assert float(sale_box_rules_get) == sale_box_rules
                assert float(purchase_box_rules_get) == purchase_box_rules
            compare_data.submit_price_button.click()
            sleep(3)
            print(compare_data.get_alert_text)

        else:
            spuid_list.append(spuid)
            print("无法打开编辑", spuid)