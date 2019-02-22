from xml.sax.handler import ContentHandler
from xml.sax import parse


# 1.sax处理方式  不太灵活,需要判断
class TestHandler(ContentHandler):
    write = False

    def startElement(self, name, attrs):
        print('标签头:', name, attrs.keys(), attrs.values())
        if name == 'page':
            self.write = True
        else:
            self.write = False

    def endElement(self, name):
        print('标签尾:', name, ",")
        self.write = False

    def characters(self, content):
        print('标签内容:', repr(content))
        if self.write:
            with open(content + '.html', 'w', encoding='utf-8') as f:
                f.write('<html>'
                        '<head>' + '头部' + '</head>'
                                          '<body>'
                                          '身体'
                                          '</body>'
                                          '</html>')

    def setDocumentLocator(self, locator):
        """文档定位器,加载xsd,dtd等文件格式"""
        print('加载dtd等')

    def startDocument(self):
        print('文档开头')

    def endDocument(self):
        print('文档末尾')


p = parse('config.xml', TestHandler())
# todo 2.dom解析方式
