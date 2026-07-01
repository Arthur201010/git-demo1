# 1.加入例外處理
# 2.重複輸入, 直到a=>exit 離開

while True:
    try:
        a=input("請輸入a: ")
        if a.lower() == "exit":
            break
        a=eval(a)
        b=eval(input("請輸入b: "))

        if a==b:
            print("a等於b")
        elif a>b:
            print(f"a>b, 差值為{a-b}")
        else:
            print(f"b>a, 差值為{b-a}")
    except Exception as e:
        print(f"輸入錯誤: {e}")