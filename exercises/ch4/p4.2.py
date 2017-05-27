def f1():
    print("f1 called")
    f2()

def f2():
    print("f2 called")


print("Main 1")
f2()
print("Main 2")
f1()
