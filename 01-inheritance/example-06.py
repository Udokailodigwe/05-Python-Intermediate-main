class A:
    def __init__(self):
        print("A.__init__")

    def func1(self):
        print("A.func1()")

    def func2(self):
        print("A.func2()")

    def func3(self):
        print("A.func3()")


class B(A):
    def __init__(self):
        super().__init__()
        print("B.__init__")

    def func1(self):
        print("B.func1()")


class C(A):
    def __init__(self):
        super().__init__()
        print("C.__init__")

    def func2(self):
        print("C.func2()")


class D(B, C):
    def __init__(self):
        super().__init__()
        print("D.__init__")

    def func3(self):
        print("D.func3()")

    def super_func3(self):
        super().func3()


if __name__ == "__main__":
    c = C()
    print(C.__mro__)
    print(C.mro())


# Python program to show the order
# in which methods are resolved

class A:
    def rk(self):
        print(" In class A")


class B:
    def rk(self):
        print(" In class B")


# classes ordering
class C(A, B):
    def __init__(self):
        print("Constructor C")


r = C()

# it prints the lookup order
print(C.__mro__)
print(C.mro())