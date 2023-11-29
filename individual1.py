#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def tag_decorator(tag="h1"):
    def decorator(func):
        def wrapper(text):
            result = func(text)
            return f"<{tag}>{result}</{tag}>"

        return wrapper

    return decorator


@tag_decorator(tag="div")
def lowercase_text(text):
    return text.lower()


if __name__ == '__main__':
    result = lowercase_text(input("Введите строку: "))
    print(result)
