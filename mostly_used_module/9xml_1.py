from xml.parsers.expat import ParserCreate
from urllib import request


class SaxXmlTest(object):
    result ={} # 这里可以把key：forecast 初始化
    result['forecast'] = []
    def handler_start(self, name, attrs):
        if name == 'yweather:location':
            for k in attrs:
                if k =='city':
                    self.result['city'] = attrs['city']
        elif name == 'yweather:forecast':
            self.result['forecast'].append(attrs)

def parseXml(xml_str):
    handler = SaxXmlTest()
    parse = ParserCreate()
    parse.StartElementHandler = handler.handler_start
    parse.Parse(xml_str)
    result = handler.result
    return result # 这里可以直接返回handler.result


URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(URL, timeout=4) as f:
    data = f.read()

result = parseXml(data.decode('utf-8'))
assert result['city'] == 'Beijing'

# 不甚满意
'''
sax方式 解析 xml 的简单代码
from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)

xml = r"<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>"


handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)
'''