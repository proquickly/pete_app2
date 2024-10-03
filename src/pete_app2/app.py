#!/usr/bin/env python
# -*- coding: utf-8 -*-

valid_html = """
<html>
<h1>
blah
</h1>
</html>
"""

print(valid_html)  # Prints the content of valid_html

invalid_html = """
<html>
</h1>
</h1>
"""

print(invalid_html)  # Prints the content of invalid_html


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, stack_item):
        self.stack.append(stack_item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()


def html_checker(html):
    checker = Stack()
    for line in html.split("\n"):
        if "<" in line and ">" in line:
            tag = line[line.index('<') + 1:line.index('>')]
            if tag.startswith('/'):  # This is a close tag
                if checker.is_empty():
                    return False
                elif tag[1:] != checker.pop():
                    return False
            else:  # This is an open tag
                checker.push(tag)
    return checker.is_empty()


if __name__ == "__main__":
    for html in [valid_html, invalid_html]:
        print(html_checker(html))
