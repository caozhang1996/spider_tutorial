import re
import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoSuchWindowException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui  import WebDriverWait
from selenium.webdriver.support import expected_conditions as  EC

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)

def search():
    try:
        browser.get('https://www.58.com')
        input_ = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#keyword')))   # 搜索框
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#searchbtn'))) # 搜索按钮
        input_.send_keys('武汉绿植租赁公司')
        button.click()
    except TimeoutException:
        search()    # 超时了重新请求一次就行了（递归）


def next_page(page_number):
    try:
        next_page_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#infolist > div.pager > a.next')))  # 确定按钮
        next_page_button.click()
        # 判断翻页是否成功
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#infolist > div.pager > strong > span'), str(page_number)))
    except TimeoutException:
        next_page(page_number)


def get_data():
    try:
        for i in range(1, 18):
            print('i=', i)
            num_to_str = int(1 + (i * 2))
            # browser.find_element_by_css_selector('#jingzhun > tbody > tr:nth-child(%d) > td.t > div > a' % num_to_str).click()
            data_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#jingzhun > tbody > tr:nth-child(%d) > td.t > div > a' % num_to_str)))
            data_button.click()
            time.sleep(2)

            # 窗口句柄
            handles = browser.window_handles
            # print(handles)
            browser.switch_to.window(handles[1])


            address = browser.find_element_by_css_selector(
                '#basicinfo > div.infocard__container.haveswitch > div.infocard__container__item.infocard__container__item--shopaddress > div.infocard__container__item__main') # 商家地址
            class_ = browser.find_element_by_css_selector(
                '#basicinfo > div.infocard__container.haveswitch > div:nth-child(2) > div.infocard__container__item__main')  # 经营类别
            # service_area = browser.find_element_by_css_selector(
            #     '#basicinfo > div.infocard__container.haveswitch > div:nth-child(3) > div.infocard__container__item__main') # 服务区域
            contact = browser.find_element_by_css_selector(
                '#basicinfo > div.infocard__container.haveswitch > div.infocard__container__item.infocard__container__item--contact > div.infocard__container__item__main') # 联系人

            time.sleep(2)
            browser.find_element_by_xpath('//*[@id="view-connect"]').click()
            phone = browser.find_element_by_css_selector('.num_cont')   # 联系电话

            datas = {'商家地址': address.text,
                     '经营类别': class_.text,
                     # '服务区域': service_area.text,
                     '联系人': contact.text,
                     '联系电话': phone.text,
                     }
            with open('plant_company_info.txt', 'w') as f:
                for key in datas:
                    f.write(key + ":" + datas[key] + '\t')
                f.write('\n')
            print(datas)
            browser.close()    # 关闭当前窗口
            browser.switch_to.window(handles[0])
    except (TimeoutException, NoSuchElementException, NoSuchWindowException):
        get_data()

def main():
    total_pages_number = 20
    search()
    get_data()
    for i in range(2, total_pages_number + 1):
        next_page(i)
        get_data()


if __name__ == '__main__':
    main()

