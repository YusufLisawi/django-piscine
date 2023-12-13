#!/usr/bin/python3

from elements import *


class Page:
    def __init__(self, elem: Elem()) -> None:
        if not isinstance(elem, Elem):
            raise Elem.ValidationError()
        self.elem = elem

    def __str__(self) -> str:
        result = ""
        if isinstance(self.elem, Html):
            result += "<!DOCTYPE html>\n"
        result += str(self.elem)
        return result

    def write_to_file(self, path: str) -> None:
        f = open(path, "w")
        f.write(self.__str__())

    def is_valid(self) -> bool:
        return self.__recursive_check(self.elem)

    def __recursive_check(self, elem: Elem()) -> bool:
        if not (isinstance(elem, (Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul, Ol, Li,
                                  H1, H2, P, Div, Span, Hr, Br)) or type(elem) == Text):
            return False
        if type(elem) == Text or isinstance(elem, Meta):
            return True
        if isinstance(elem, Html) and len(elem.content) == 2 \
                and type(elem.content[0]) == Head and type(elem.content[1]) == Body:
            if (all(self.__recursive_check(el) for el in elem.content)):
                return True
        elif isinstance(elem, Head) and [isinstance(el, Title) for el in elem.content].count(True) == 1:
            if (all(self.__recursive_check(el) for el in elem.content)):
                return True
        elif isinstance(elem, (Body, Div)) and \
                all([isinstance(el, (H1, H2, Div, Table, Ul, Ol, Span)) or
                    type(el) == Text for el in elem.content]):
            if (all(self.__recursive_check(el) for el in elem.content)):
                return True
        elif isinstance(elem, (Title, H1, H2, Li, Th, Td)) and \
                len(elem.content) == 1 and type(elem.content[0]) == Text:
            return True
        elif isinstance(elem, P) and \
                all([isinstance(el, Text) for el in elem.content]):
            return True
        elif isinstance(elem, Span) and \
                all([isinstance(el, (Text, P)) for el in elem.content]):
            if (all(self.__recursive_check(el) for el in elem.content)):
                return True
        elif isinstance(elem, (Ul, Ol)) and len(elem.content) > 0 and \
                all([isinstance(el, Li) for el in elem.content]):
            if (all(self.__recursive_check(el) for el in elem.content)):
                return True
        elif isinstance(elem, Tr) and len(elem.content) > 0 and\
                all([isinstance(el, (Th, Td)) for el in elem.content]) and \
                all([type(el) == type(elem.content[0]) for el in elem.content]):
            return True
        elif isinstance(elem, Table) and \
                all([isinstance(el, Tr) for el in elem.content]):
            return True
        return False


def print_test(target: Page, toBe: bool):
    print("================START===============")
    print(str(target))
    print("===============IS_VALID=============")
    assert target.is_valid() == toBe
    print("{:^36s}".format(str(target.is_valid())))
    print("=================END================")


def test_Table():
    print("\n%{:=^34s}%\n".format("Table"))
    target = Page(Table())
    print_test(target, True)
    target = Page(
        Table(
            [
                Tr(),
            ]))
    print_test(target, True)
    target = Page(
        Table(
            [
                H1(
                    Text("Hello World!")
                ),
            ]))
    print_test(target, False)


def test_Tr():
    print("\n%{:=^34s}%\n".format("Tr"))
    target = Page(Tr())
    print_test(target, False)
    target = Page(
        Tr(
            [
                Th(Text("title")),
                Th(Text("title")),
                Th(Text("title")),
                Th(Text("title")),
                Th(Text("title")),
            ]))
    print_test(target, True)
    target = Page(
        Tr(
            [
                Td(Text("content")),
                Td(Text("content")),
                Td(Text("content")),
                Td(Text("content")),
                Td(Text("content")),
                Td(Text("content")),
            ]))
    print_test(target, True)
    target = Page(
        Tr(
            [
                Th(Text("title")),
                Td(Text("content")),
            ]))
    print_test(target, False)


def test_Ul_OL():
    print("\n%{:=^34s}%\n".format("Ul_OL"))
    target = Page(
        Ul()
    )
    print_test(target, False)
    target = Page(
        Ol()
    )
    print_test(target, False)
    target = Page(
        Ul(
            Li(
                Text('test')
            )
        )
    )
    print_test(target, True)
    target = Page(
        Ol(
            Li(
                Text('test')
            )
        )
    )
    print_test(target, True)
    target = Page(
        Ul([
            Li(
                Text('test')
            ),
            Li(
                Text('test')
            ),
        ])
    )
    print_test(target, True)
    target = Page(
        Ol([
            Li(
                Text('test')
            ),
            Li(
                Text('test')
            ),
        ])
    )
    print_test(target, True)
    target = Page(
        Ul([
            Li(
                Text('test')
            ),
            H1(
                Text('test')
            ),
        ])
    )
    print_test(target, False)
    target = Page(
        Ol([
            Li(
                Text('test')
            ),
            H1(
                Text('test')
            ),
        ])
    )
    print_test(target, False)


def test_Span():
    print("\n%{:=^34s}%\n".format("Span"))
    target = Page(
        Span()
    )
    print_test(target, True)
    target = Page(
        Span([
            Text("Hello?"),
            P(Text("World!")),
        ])
    )
    print_test(target, True)
    target = Page(
        Span([
            H1(Text("World!")),
        ])
    )
    print_test(target, False)


def test_P():
    print("\n%{:=^34s}%\n".format("P"))
    target = Page(
        P()
    )
    print_test(target, True)
    target = Page(
        P([
            Text("Hello?"),
        ])
    )
    print_test(target, True)
    target = Page(
        P([
            H1(Text("World!")),
        ])
    )
    print_test(target, False)


def test_Title_H1_H2_Li_Th_Td():
    print("\n%{:=^34s}%\n".format("H1_H2_Li_Th_Td"))
    for c in [H1, H2, Li, Th, Td]:
        target = Page(
            c()
        )
        print_test(target, False)
        target = Page(
            c([
                Text("Hello?"),
            ])
        )
        print_test(target, True)
        target = Page(
            c([
                H1(Text("World!")),
            ])
        )
        print_test(target, False)
        target = Page(
            c([
                Text("Hello?"),
                Text("Hello?"),
            ])
        )
        print_test(target, False)


def test_Body_Div():
    print("\n%{:=^34s}%\n".format("Body_Div"))
    for c in [Body, Div]:
        target = Page(
            c()
        )
        print_test(target, True)
        target = Page(
            c([
                Text("Hello?"),
            ])
        )
        print_test(target, True)
        target = Page(
            c([
                H1(Text("World!")),
            ])
        )
        print_test(target, True)
        target = Page(
            c([
                Text("Hello?"),
                Span(),
            ])
        )
        print_test(target, True)
        target = Page(
            c([
                Html(),
                c()
            ])
        )
        print_test(target, False)


def test_Title():
    print("\n%{:=^34s}%\n".format("Title"))
    target = Page(
        Title()
    )
    print_test(target, False)
    target = Page(
        Title([
            Title(Text("Hello?")),
        ])
    )
    print_test(target, True)
    target = Page(
        Title([
            Title(Text("Hello?")),
            Title(Text("Hello?")),
        ])
    )
    print_test(target, False)


def test_Html():
    print("\n%{:=^34s}%\n".format("Html"))
    target = Page(
        Html()
    )
    print_test(target, False)
    target = Page(
        Html([
            Head([
                Title(Text("Hello?")),
            ]),
            Body([
                H1(Text("Hello?")),
            ])
        ])
    )
    print_test(target, True)
    target = Page(
        Html(
            Div()
        )
    )
    print_test(target, False)


def test_Elem():
    print_test(Page(Elem()), False)


def test_write_to_file(target: Page, path: str):
    print("================START===============")
    print(str(target))
    print("==========WRITE_TO_FILE=============")
    target.write_to_file(path)
    print("{:^36s}".format(path))
    print("=================END================")


def test():
    test_Table()
    test_Tr()
    test_Ul_OL()
    test_Span()
    test_P()
    test_Title_H1_H2_Li_Th_Td()
    test_Body_Div()
    test_Html()
    test_Elem()
    test_write_to_file(
        Page(Html([Head(Title(Text("hello world!"))),
             Body(H1(Text("HELLO WORLD!")))])),
        "test_write_to_file.html")


if __name__ == '__main__':
    test()