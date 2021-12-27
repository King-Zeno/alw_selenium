from time import sleep
from poium import Page, Element, Elements
from poium import Browser
import xlrd,pytest
from selenium import webdriver

def get_data(file_name):
    rows = []
    book = xlrd.open_workbook(file_name)
    sheet = book.sheet_by_index(1)
    for row_idx in range(1, sheet.nrows):
        rows.append(list(sheet.row_values(row_idx, 0, sheet.ncols)))
    print(rows)
    return rows

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
    create_brand_button = Element(xpath="/html/body/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/a/span", describe="创建品牌按钮")
    brand_name_input = Element(xpath="/html/body/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/form/div/div[2]/div/div/div/div/div/input", describe="输入品牌名称")
    sort_num = Element(xpath="/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[2]/form/div/div[3]/div/div/div/div/div/div[2]/input", describe="排序")
    remark_input = Element(xpath="/html/body/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/form/div/div[5]/div/div/div/div/div/textarea", describe="备注")
    create_brand_submit = Element(xpath="/html/body/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/button/span", describe="提交")

value = get_data('goods_data.xlsx')
@pytest.mark.parametrize('data', value)
def test_login(data):
    goods_classes = data[0]


    dr = webdriver.Chrome(r'D:\Work\QA\selenium\webdriver\chromedriver.exe')
    dr.maximize_window()
    create = loginPage(dr)
    create.open("http://amp.test.alwooo.com:8497/")
    create.mobile_number.send_keys("15575540001")
    create.password.send_keys("123456")
    create.login_button.click()
    sleep(2)
    create.brand_manager.click()
    create.brand_manager_next.click()
    create.create_brand_button.click()
    sleep(1)
    create.brand_name_input.send_keys(data[5])
    create.sort_num.send_keys(1)
    create.remark_input.send_keys("1234567890ksdd")
    create.create_brand_submit.click()
    sleep(1)

    dr.close()