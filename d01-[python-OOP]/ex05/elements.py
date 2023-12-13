from elem import *

class Html(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('html', attr, content, 'double')

class Head(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('head', attr, content, 'double')

class Body(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('body', attr, content, 'double')

class Title(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('title', attr, content, 'double')

class Meta(Elem):
    def __init__(self, attr={}):
        super().__init__('meta', attr, None, 'simple')

class Img(Elem):
    def __init__(self, attr={}):
        super().__init__('img', attr, None, tag_type='simple')

class Table(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('table', attr, content, 'double')

class Th(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('th', attr, content, 'double')

class Tr(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('tr', attr, content, 'double')

class Td(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('td', attr, content, 'double')

class Ul(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('ul', attr, content, 'double')

class Ol(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('ol', attr, content, 'double')

class Li(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('li', attr, content, 'double')

class H1(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('h1', attr, content, 'double')

class H2(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('h2', attr, content, 'double')

class P(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('p', attr, content, 'double')

class Div(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('div', attr, content, 'double')

class Span(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('span', attr, content, 'double')

class Hr(Elem):
    def __init__(self, attr={}):
        super().__init__('hr', attr, None, 'simple')

class Br(Elem):
    def __init__(self, attr={}):
        super().__init__('br', attr, None, 'simple')

if __name__ == "__main__":
    print(Html([
        Head(Title(Text('"Hello ground!"'))), 
        Body([
            H1(Text('"Oh no, not again!"')),
            Img({'src' : 'http://i.imgur.com/pfp3T.jpg'})
            ])]))