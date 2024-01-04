class A:
    var1 = "I am in class A"
    def __init__(self):
        self.var1 = "I am in class A's Constructor."
        self.special = "Special"
class B(A):
    var2 = "I am in class B"
    def __init__(self):
        self.var1 = "I am in class B's Constructor."
        super().__init__()
        print(super().var1)
a = A()
b = B()
print(b.special)
print(b.var1)