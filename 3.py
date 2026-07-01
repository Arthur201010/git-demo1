a=eval(input("請輸入a: "))
b=eval(input("請輸入b: "))

if a==b:
    print("a等於b")
elif a>b:
    print(f"a>b, 差值為{a-b}")
else:
    print(f"b>a, 差值為{b-a}")