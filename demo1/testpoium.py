from time import sleep
from poium import Page, Element, Elements
from poium import Browser
from selenium import webdriver

# page层定义
class BaiduPage(Page):
    input = Element(id_="kw", describe="搜索输入框")
    button = Element(id_="su", describe="搜索按钮")
    results = Elements(xpath="//div/h3/a", describe="搜索结果")


dr = webdriver.Chrome(r'D:\Work\QA\selenium\webdriver\chromedriver.exe')
page = BaiduPage(dr)
page.get("https://www.baidu.com")
page.input.send_keys("baidu")
page.button.click()
sleep(2)

elem = page.results
for e in elem:
    print(e.text)

dr.close()