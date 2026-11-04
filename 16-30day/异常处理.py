#1.捕获特定的错误:文件找不到(FileNotFoundError)
print("=== 第一部分:基础异常测试 ===")
try:
    with open("no_such_file.txt", "r", encoding="utf-8") as f:
        content = f.read()
except FileNotFoundError:
    print("错误:你要找的文件不存在!")

#2.捕获特定的错误:除数为零(ZeroDivisionError)
try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("错误:除数不能为0!")

#3.万能兜底:捕获所有未知错误(Exception)
try:
    x = int("abc")
except Exception as e:
    print(f"发生了一个未知错误,具体原因是:{e}")
print("\n" + "=" * 40 + "\n")

print("=== 第二部分:输入校验与无限重试 ===")
while True:
    user_input = input("请输入一个数字(随便输入字母测试一下防弹衣):")
    try:
        num = float(user_input)
        print(f"成功!你输入的数字是:{num}")
        break
    except ValueError:
        print("错误:这不是数字,请重新输入!\n")

print("\n--- 附加挑战:计算器防错版 ---")
while True:
    a_str = input("请输入第一个数字(输入q退出):")
    if a_str == "q":
        break
    try:
        a = float(a_str)
        b = float(input("请输入第二个数字:"))
        result = a / b
        print(f"计算结果:{a}/{b}={result:.2f}")
    except ValueError:
        print("错误:请输入有效的数字!\n")
    except ZeroDivisionError:
        print("错误:除数不能为0,请重新输入!\n")
