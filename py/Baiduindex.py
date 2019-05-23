# !/usr/bin/python3.4
# -*- coding: utf-8 -*-




import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image


#import  cv2


num = [0]
jd = [0]
code = [0]
account = []
# 打开浏览器
def openbrowser():
    global browser

    # https://passport.baidu.com/v2/?login
    url = "https://passport.baidu.com/v2/?login&tpl=mn&u=http%3A%2F%2Fwww.baidu.com%2F"
    # 打开谷歌浏览器
    # Firefox()
    # Chrome()
    option = webdriver.FirefoxOptions()
    option.add_argument('--user-data-dir=C:\\Users\\LMR\\AppData\\Local\\Google\\Chrome\\User Data')  # 设置成用户自己的数据目录
    # browser = webdriver.Chrome(chrome_options=option)
    browser = webdriver.Firefox(firefox_options=option)
    # browser = webdriver.Chrome()
    # 输入网址
    browser.get(url)
    # 打开浏览器时间
    # print("等待10秒打开浏览器...")
    # time.sleep(10)

    browser.find_element_by_id("TANGRAM__PSP_3__footerULoginBtn").click()
    # 找到id="TANGRAM__PSP_3__userName"的对话框
    # 清空输入框
    browser.find_element_by_id("TANGRAM__PSP_3__userName").clear()
    browser.find_element_by_id("TANGRAM__PSP_3__password").clear()
    # account = ['18655654429', 'lqh959260.']
    # account = ['1341709851@qq.com', 'lqh959260']

    browser.find_element_by_id("TANGRAM__PSP_3__userName").send_keys(account[2][0])
    browser.find_element_by_id("TANGRAM__PSP_3__password").send_keys(account[2][1])
    time.sleep(10)
    # 点击登陆登陆
    # id="TANGRAM__PSP_3__submit"
    browser.find_element_by_id("TANGRAM__PSP_3__submit").click()
    # 最大化窗口
    time.sleep(2)
    browser.maximize_window()
    time.sleep(2)
    js = 'window.open("http://index.baidu.com");'
    browser.execute_script(js)
    # 新窗口句柄切换，进入百度指数
    # 获得当前打开所有窗口的句柄handles
    # handles为一个数组
    handles = browser.window_handles
    # print(handles)
    # 切换到当前最新打开的窗口
    browser.switch_to_window(handles[-1])
    # browser.close()
    # 在新窗口里面输入网址百度指数
    # 清空输入框
    time.sleep(6)
    # 等待登陆10秒
    # print('等待登陆10秒...')
    # time.sleep(10)
    print("等待网址加载完毕...")




def getindex(keyword,startyear,startm,eyear,em):

    time.sleep(2)

    # 这里开始进入百度指数
    # 要不这里就不要关闭了，新打开一个窗口
    # http://blog.csdn.net/DongGeGe214/article/details/52169761
    # 新开一个窗口，通过执行js来新开一个窗口
    browser.find_element_by_id("schword").clear()
    # 写入需要搜索的百度指数
    browser.find_element_by_id("schword").send_keys(keyword)
    time.sleep(1)
   # print keyword
    # 点击搜索
    # <input type="submit" value="" id="searchWords" onclick="searchDemoWords()">
    browser.find_element_by_id("schsubmit").click()
    time.sleep(3)

    # 构造天数
    # sel = '//a[@rel="' + str(day) + '"]'
    sel = '//a[@rel="diy"]'
    browser.find_element_by_xpath(sel).click()
    # 太快了
    time.sleep(0.5)
    ptbs = browser.find_elements_by_xpath("//div[@id='auto_gsid_16']/div[@class='ptb05']")
    ptbs[0].find_element_by_xpath("//span[@class='selectA yearA']").click()
    time.sleep(0.5)
    ptbs[0].find_element_by_xpath("//div[@class='sltOpt']/a[@href='#"+str(startyear)+"']").click()
    time.sleep(0.5)
    ptbs[0].find_element_by_xpath("//span[@class='selectA monthA']").click()
    time.sleep(0.5)
    if startm<10:
        ptbs[0].find_element_by_xpath("//ul[@class='sltOpt']/li/a[@href='#0"+str(startm)+"']").click()
    else:
        ptbs[0].find_element_by_xpath("//ul[@class='sltOpt']/li/a[@href='#" + str(startm) + "']").click()
    time.sleep(0.5)

    s = ptbs[1].find_element_by_xpath("//span[@class='selectA yearA']")
    ActionChains(browser).move_to_element_with_offset(s,10,40).click().perform()
    time.sleep(0.5)
    #print eyear
    browser.find_element_by_xpath("//span[@class='selectA yearA slided']/div[@class='sltOpt']/a[@href='#" + str(eyear) + "']").click()
    time.sleep(0.5)
    m = ptbs[1].find_element_by_xpath("//span[@class='selectA monthA']")
    ActionChains(browser).move_to_element_with_offset(m, 10, 40).click().perform()
    time.sleep(0.5)
    #print em
    if em<10:
        browser.find_element_by_xpath("//span[@class='selectA monthA slided']/ul[@class='sltOpt']/li/a[@href='#0" + str(em) + "']").click()
    else:
        browser.find_element_by_xpath("//span[@class='selectA monthA slided']/ul[@class='sltOpt']/li/a[@href='#" + str(em) + "']").click()
    time.sleep(0.5)

    pbu = browser.find_elements_by_xpath("//div[@class='ptb05 pl20']/input[@class='button ml20']")
    pbu[0].click()

    xoyelement = browser.find_element_by_xpath('//li[@data-value="all"]')
    # ActionChains(browser).click(xoyelement).perform()
    time.sleep(0.5)

    # 获得坐标长宽
    # x = xoyelement.location['x']
    # y = xoyelement.location['y']
    # width = xoyelement.size['width']
    # height = xoyelement.size['height']
    # print(x,y,width,height)
    # 常用js:http://www.cnblogs.com/hjhsysu/
    # p/5735339.html
    # 搜索词：selenium JavaScript模拟鼠标悬浮
    x_0 = 3
    y_0 = 130
    # print xoyelement.location,"trend"
    # if day == "all":
    #     day = 1000000
    invert = 13.64
    day = 0
    if jd[0] == 0:
        day = 90
        invert = 13.64
    if jd[0]==1:
        day = 91
        invert = 13.49
    if jd[0] ==2:
        day = 92
        invert = 13.34
    if jd[0] ==3:
        day = 92
        invert = 13.34
    # 储存数字的数组
    index = []

    try:
        webdriver.ActionChains(browser).move_to_element(xoyelement).perform()
        # 只有移动位置xoyelement[2]是准确的
        for i in range(day - 1):
            # 坐标偏移量???
            ActionChains(browser).move_to_element_with_offset(xoyelement, x_0, y_0).perform()
            #
            time.sleep(1.5)
            # ActionChains(browser).move_to_element_with_offset(xoyelement, 0, y_0).perform()
            # #36
            # time.sleep(3)
            # 构造规则
            # <div class="imgtxt" style="margin-left:-117px;"></div>
            while (1 == 1):
                try:
                    a = browser.find_element_by_xpath("//div[@id='viewbox']")
                    locs = a.location
                    x = locs["x"]
                    if x != 0.0:
                        break
                    ActionChains(browser).move_to_element_with_offset(xoyelement, x_0+8, y_0).perform()
                    ActionChains(browser).move_to_element_with_offset(xoyelement, x_0, y_0).perform()
                except Exception as err:
                   # print i
                    ActionChains(browser).move_to_element_with_offset(xoyelement, x_0, y_0).perform()
                    continue
            time.sleep(1.5)
            # if num==89:
            #     ActionChains(browser).move_to_element_with_offset(xoyelement, x_0-8, y_0).perform()
            #     time.sleep(1)

            # 截取当前浏览器
            path = "../baidu/"+str(keyword)+ str(num[0])
            browser.save_screenshot(str(path) + ".png")
            # 打开截图切割
            im = cv2.imread(str(path) + ".png")
            # obj = cv2.imread("../baidu/obj.png")
            # pos = ac.find_template(im, obj)
            # ran = pos["rectangle"]
            # objrex = ran[2][0] - ran[0][0]
            # objrey = ran[1][1] - ran[0][1]
            # re = im[ran[0][1] + int(1.0 / 2.0 * objrey):ran[3][1],
            #      ran[0][0] + int(1.0 / 3.0 * objrex):ran[3][0] - int(1.0 / 2.0 * objrex)]
            # cv2.imwrite(str(path) + "y.png", re)
            num[0] = num[0] + 1

            # if day == 7:
            #     x_0 = x_0 + 202.33
            # elif day == 30:
            #     x_0 = x_0 + 41.68
            # elif day == 90:
            x_0 = x_0 + invert
            # elif day == 180:
            #     x_0 = x_0 + 6.78
            # elif day == 1000000:
            #     x_0 = x_0 + 3.37222222

    except Exception as err:
        print(err)
        print(num[0])
    # browser.close()
    # print(index)
    # # 日期也是可以图像识别下来的
    # # 只是要构造rangle就行，但是我就是懒
    # file = open("../baidu/index.txt", "w")
    # for item in index:
    #     file.write(str(item) + "\n")
    # file.close()



if __name__ == "__main__":
    # 每个字大约占横坐标12.5这样
    # 按照字节可自行更改切割横坐标的大小rangle
    # keyword = input("请输入查询关键字：")
    # st = input("输入查询开始年份：")
    # sm = input("输入查询开始月份：")
    # se = input("输入查询结束年份：")
    # em = input("输入查询结束月份：")
    # sel = int(input("查询7天请按0，30天请按1，90天请按2，半年请按3，全部请按4："))
    # keyword = u"300269股票"
    # sel = 2
    # day = 0
    # if sel == 0:
    #     day = 7
    # elif sel == 1:
    #     day = 30
    # elif sel == 2:
    #     day = 90
    # elif sel == 3:
    #     day = 180
    # elif sel == 4:
    #     day = "all"

    openbrowser()
    # code[0] = 2
    # getindex(11, 2017, 1, 2017, 2)
    keyword = []
    for i in range(100):
        keyword.append(300052+i)
    for i in range(100):
        sm = 1
        em = 3
        num[0] = 0
        for j in range(4):
            jd[0] = j
            getindex(keyword[i], 2017, sm, 2017, em)
            sm = sm + 3
            em = em + 3
            time.sleep(1)



    # im = Image.open("../baidu/0zoom.jpg")
    # imgry = im.convert('L')  # 图像加强，二值化
    # sharpness = ImageEnhance.Contrast(imgry)  # 对比度增强
    # sharp_img = sharpness.enhance(2.0)
    # sharp_img.save("../baidu/0000zoom.jpg")
    # index = []

    # print index
    # file = open("../baidu/index.txt", "w")
    # for item in index:
    #     file.write(str(item) + "\n")
    # file.close()
    #100042 0 1 2 3    100049   51