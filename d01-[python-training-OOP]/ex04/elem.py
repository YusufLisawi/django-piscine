#!/usr/bin/python3

class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.

    Because directly using str class was too mainstream.
    """

    def __str__(self):
        """
        Do you really need a comment to understand this method?..
        """
        string = super().__str__()
        replace_dict = {
            '<' : '&lt;',
            '>' : '&gt;',
            '"' : '&quot;',
            '\n' : '\n<br />\n',
        }
        for old, new in replace_dict.items():
            string = string.replace(old, new)
        return string

class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """
    
    class ValidationError(Exception):
        def __init__(self) -> None:
            super().__init__("incorrect behaviour.")

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        """
        __init__() method.

        Obviously.
        """
        if (content and not Elem.check_type(content)) or tag_type not in ['double', 'simple']:
            raise Elem.ValidationError()
        self.tag = tag
        self.attr = attr
        self.content = []
        self.content = self.add_content(content)
        self.tag_type = tag_type

    def __str__(self):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """
        result = f'<{self.tag}{self.__make_attr()}'
        if self.tag_type == 'double':
            result += '>' + self.__make_content()
            result += f'</{self.tag}>'

        elif self.tag_type == 'simple':
            result += f'/>'
        return result

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ''
        for k, v in sorted(self.attr.items()):
            result += ' ' + str(k) + '="' + str(v) + '"'
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """

        if len((self.content)) == 0:
            return ''
        result = '\n'
        for elem in self.content:
            if (len(str(elem)) != 0):
                result += str(elem) + '\n'
        return result

    def add_content(self, content):
        if not content:
            self.content.append('')
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))
    
    def __len__(self):
        return len(str(self))


if __name__ == '__main__':
    print(Text('\n'))
    print(Elem())
    # print(Elem('div', {}, None, 'double'))
    # print(Elem(tag='body', attr={}, content=Elem(), tag_type='double'))
    # print(Elem(content=Elem()))
    # print(Elem(content=[Text('foo'), Text('bar'), Elem()]))
