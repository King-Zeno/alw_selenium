import re
import pytesseract
from PIL import Image
from selenium import webdriver
import time

class VerificationCode:
    def __init__(self):
        '''chrome_driver = r'D:\Work\QA\selenium\webdriver\chromedriver.exe'
        options = webdriver.ChromeOptions()
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option("excludeSwitches", ['enable-automation'])
        self.driver = webdriver.Chrome(options=options, executable_path=chrome_driver)
        self.find_element = self.driver.find_element_by_css_selector
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)'''
        pass

    '''def get_pictures(self):
        self.driver.get('http://store.test.alwooo.com:8167')  # 打开登陆页面
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
        image_obj.show()  # 打开切割后的完整验证码
        self.driver.close()  # 处理完验证码后关闭浏览器
        return image_obj'''

    def processing_image(self, image_obj):
        #image_obj = self.get_pictures()  # 获取验证码
        img = image_obj.convert("L")  # 转灰度
        pixdata = img.load()
        w, h = img.size
        threshold = 160  # 该阈值不适合所有验证码，具体阈值请根据验证码情况设置
        # 遍历所有像素，大于阈值的为黑色
        for y in range(h):
            for x in range(w):
                if pixdata[x, y] < threshold:
                    pixdata[x, y] = 0
                else:
                    pixdata[x, y] = 255
        return img

    def delete_spot(self, image_obj):
        images = self.processing_image(image_obj)
        data = images.getdata()
        w, h = images.size
        black_point = 0
        for x in range(1, w - 1):
            for y in range(1, h - 1):
                mid_pixel = data[w * y + x]  # 中央像素点像素值
                if mid_pixel < 50:  # 找出上下左右四个方向像素点像素值
                    top_pixel = data[w * (y - 1) + x]
                    left_pixel = data[w * y + (x - 1)]
                    down_pixel = data[w * (y + 1) + x]
                    right_pixel = data[w * y + (x + 1)]
                    # 判断上下左右的黑色像素点总个数
                    if top_pixel < 10:
                        black_point += 1
                    if left_pixel < 10:
                        black_point += 1
                    if down_pixel < 10:
                        black_point += 1
                    if right_pixel < 10:
                        black_point += 1
                    if black_point < 1:
                        images.putpixel((x, y), 255)
                    black_point = 0
        # images.show()
        return images

    def image_str(self, image_obj):
        image = self.delete_spot(image_obj)
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"  # 设置pyteseract路径
        result = pytesseract.image_to_string(image)  # 图片转文字
        resultj = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", result)  # 去除识别出来的特殊字符
        result_four = resultj[0:4]  # 只获取前4个字符
        # print(resultj)  # 打印识别的验证码
        return result_four

'''if __name__ == '__main__':
    a = VerificationCode()
    print(a.image_str())'''