class A:
    def a_method(self):
        print("sample")

    def method(self):
        print("A method")


class B(A):
    def __init__(self):
        super().__init__()

    def method(self):
        print("B method")


class C(A):
    def method(self):
        print("c method")


class D(B, C):
    pass


b = B()
b.a_method()

print(B.mro())
print(D.mro())