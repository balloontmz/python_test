from html.parser import HTMLParser
import re
from urllib import request
# parctice


class MyHTMLParser(HTMLParser):

    def __init__(self):
        super(MyHTMLParser, self).__init__()
        self.information = []
        self.flag = 0
        self.__dataname = 0

    def handle_starttag(self, tag, attrs):
        if tag == 'ul' and re.match(r'list-recent-events', attrs[0][1]):
            self.flag = 1
        if self.flag == 1 and tag == 'a':
            self.__dataname = 'title'
        elif self.flag == 1 and tag == 'time':
            self.__dataname = 'time'
        elif self.flag == 1 and tag == 'span' and re.match(r'say-no-more', attrs[0][1]):
            self.__dataname = 'year'
        elif self.flag == 1 and tag == 'span':
            self.__dataname = 'location'

    def handle_endtag(self, tag):
        if tag == 'ul' and self.flag == 1:
            self.flag = 0

    def handle_data(self, data):
        if self.__dataname and self.flag == 1:
            if self.__dataname == 'title':
                self.information.append({self.__dataname: data})
            else:
                self.information[-1][self.__dataname] = data
        self.__dataname = 0


URL = 'https://www.python.org/events/python-events/'
with request.urlopen(URL) as f:
    data_ = f.read().decode('utf-8')
parse = MyHTMLParser()
parse.feed(data_)
for attrs_ in parse.information:
    print('-----------------------------------------------------')
    for item in attrs_:
        print('%s: %s' % (item, attrs_[item]))


"""
# html解析的简单实现代码
from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')
"""