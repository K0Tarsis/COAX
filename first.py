import hashlib


def foo(s="Python Bootcamp"):
    b = s.encode('utf-8')
    return hashlib.md5(b).hexdigest()


if __name__ == "__main__":
    print(foo())
