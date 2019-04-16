
from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

import requests     # http请求库，用来做模拟请求的
import re           # 用于实现正则表达式

# # 爬知乎
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36'}
# response = requests.get('http://www.zhihu.com/explore', headers=headers)
# print(response.text)

# data = {'name': 'germey', 'age': '22'}
# response = requests.post('http://httpbin.org/post', data=data)
# print(response.text)



# 正则表达式：
# 正则表达式是对字符串操作的一种逻辑公式，就是用事先定义好的一些特定字符、及这些特定字符的组合，组成一个
# “规则字符串”，这个“规则字符串”用来表达对字符串的一种过滤逻辑


# re.match
# match 用来检测你写的正则表达式与传入的字符串是否是匹配的
# 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配的话，match()就返回none。

# 最常规的匹配
def common_match():
    content = 'Hello 123 4567 World_This is a Regex Demo'
    print(len(content))
    result = re.match('^Hello\s\d{3}\s\d{4}\s\w{10}.*Demo$', content)
    print(result)
    print(result.group())
    print(result.span())      #span返回长度

# 泛匹配
def match_1():
    content = 'Hello 123 4567 World_This is a Regex Demo'
    print(len(content))
    result = re.match('^Hello.*Demo$', content)
    print(result)
    print(result.group())
    print(result.span())  # span返回长度

# 匹配目标
def match_2():
    content = 'Hello 123 4567 World_This is a Regex Demo'
    print(len(content))
    result = re.match('Hello\s(\d+)\s(\d+)\s(\w+).*Demo', content)   # 不用^ $符号也是可以的
    print(result)
    print(result.group(3))   #使用group(1) group(2)来匹配我们想得到的目标
    print(result.span())     # span返回长度

# 贪婪匹配
def match_3():
    content = 'Hello 123 4567 World_This is a Regex Demo'
    print(len(content))
    result = re.match('H.*(\d+).*Demo', content)      # 第一个.*匹配的是ello 123 456
    print(result)
    print(result.group(1))
    print(result.span())

# 非贪婪匹配
def match_4():
    content = 'Hello 123 4567 World_This is a Regex Demo'
    print(len(content))
    result = re.match('H.*?(\d+)\s(\d+).*Demo', content)      # 第一个.*匹配的是ello
    print(result)
    print(result.group(2))
    print(result.span())


# re.search
# re.search扫描整个字符串并返回第一个成功的匹配, search不需要从起始位置开始
def search():
    content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
    result = re.search('Hello.*?(\d+).*?Demo', content)
    print(result)
    print(result.group(1))


# 匹配演练
def practice():

    html = '''<div id="songs-list">
        <h2 class="title">经典老歌</h2>
        <p class="introduction">
            经典老歌列表
        </p>
        <ul id="list" class="list-group">
            <li data-view="2">一路上有你</li>
            <li data-view="7">
                <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
            </li>
            <li data-view="4" class="active">
                <a href="/3.mp3" singer="齐秦">往事随风</a>
            </li>
            <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
            <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
            <li data-view="5">
                <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
            </li>
        </ul>
    </div>'''
    # 将齐秦 往事随风找出来
    result1 = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)   # .*不能匹配换行符， 需加上re.S才能匹配换行符
    print(result1.group(1), result1.group(2))

    result2 = re.search('<li.*?singer="(.*?)">(.*?)</a>', html, re.S)  #没有active关键字，则只能匹配到第一个
    print(result2.group(1), result2.group(2))

    result3 = re.search('<li.*?singer="(.*?)">(.*?)</a>', html)  # 没有re.S，则不能匹配到换行符
    print(result3.group(1), result3.group(2))


# re.findall
# 搜索字符串，以列表形式返回全部能匹配到的字串
def find_str():

    html = '''<div id="songs-list">
            <h2 class="title">经典老歌</h2>
            <p class="introduction">
                经典老歌列表
            </p>
            <ul id="list" class="list-group">
                <li data-view="2">一路上有你</li>
                <li data-view="7">
                    <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
                </li>
                <li data-view="4" class="active">
                    <a href="/3.mp3" singer="齐秦">往事随风</a>
                </li>
                <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
                <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
                <li data-view="5">
                    <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
                </li>
            </ul>
        </div>'''
    # 任贤齐，齐秦，beyond，陈慧琳，邓丽君所在的行有相同的形式
    results1 = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(\w+)</a>', html, re.S)
    for result1 in results1:
        print(result1[0], result1[1], result1[2])

    # 将一路上有你也提取出来
    results2 = re.findall('<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>', html, re.S)
    for result2 in results2:
        print(result2[1])


# 爬取豆瓣网站信息（示例demo）
def pa_douban():
    content = requests.get('http://book.douban.com/').text
    pattern = re.compile('<li.*?cover.*?href="(.*?)".*?tittle="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>', re.S)
    results = re.search(pattern, content)
    print(results)

# if __name__ == '__main__':
#     pa_douban()


content = requests.get('https://book.douban.com/').text
# print(content)
pattern = re.compile('<li.*?cover.*?href="(.*?)".*?more-meta.*?title">(.*?)</h4>.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>', re.S)
results = re.search(pattern, content)
#print(results)
print(results.group(1), results.group(2),results.group(3), results.group(4))
# for result in results:
#     url, name, author, date = result
#     author = re.sub('\s', '', author)
#     date = re.sub('\s', '', date)
#     print(url, name, author, date)