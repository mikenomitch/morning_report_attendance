def greet(name, enthusiasm):
    if enthusiasm == 0:
        print("hi " + name)
    if enthusiasm == 1:
        print("hey " + name + "!")
    if enthusiasm == 2:
        print("omg, it's " + name + "!")


greet("mike", 0)
greet("bob", 1)
greet("jamie", 2)
