from html.parser import HTMLParser
from urllib import request
import re

class MyHTMLParser(HTMLParser):
    flag = 0
    res = []
    is_get_data = 0

    def handle_starttag(self, tag, attrs):
        # 首先找到包裹事件的元素
        if tag == 'ul':
            for attr in attrs:
                if re.match(r'list-recent-events', attr[1]):
                    self.flag = 1

        # 处理包裹事件名称的a元素
        if tag == 'a' and self.flag == 1:
            self.is_get_data = 'title'

        # 处理时间的time元素
        if tag == 'time' and self.flag == 1:
            self.is_get_data = 'time'

        # 处理包裹地点的time元素
        if tag == 'span' and self.flag == 1:
            self.is_get_data = 'addr'

    def handle_endtag(self, tag):
        if self.flag == 1 and tag == 'ul':
            self.flag = 0

    def handle_data(self, data):
        if self.is_get_data and self.flag == 1:
            if self.is_get_data == 'title':
                self.res.append({self.is_get_data: data})
            else:
                self.res[len(self.res) - 1][self.is_get_data] = data
            self.is_get_data = None


parser = MyHTMLParser()

with request.urlopen('https://www.python.org/events/python-events/') as f:
    data = f.read().decode('utf-8')

parser.feed(data)
for item in MyHTMLParser.res:
    print('---------------')
    for k,v in item.items():
        print("%s : %s" % (k,v))