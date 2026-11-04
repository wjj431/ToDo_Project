# ==========================================
# 第 18-21 天：文件读写与异常处理
# ==========================================

# 1. 写入文件（演示 w 和 a 模式）
def save_data_to_file(filename, data_list):
    print(f"\n--- 正在保存数据到 {filename} ---")
    # 使用 "w" 模式：如果文件存在则清空，不存在则创建
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for item in data_list:
                f.write(f"{item}\n")  # \n 是为了换行
        print("✅ 数据保存成功！")
    except Exception as e:
        print(f"❌ 保存失败，发生错误：{e}")


# 2. 读取文件（演示 r 模式 + 异常处理）
def read_data_from_file(filename):
    print(f"\n--- 正在从 {filename} 读取数据 ---")
    result_list = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                # line 带有 \n，必须 strip 掉，再转成数字
                num = float(line.strip())
                result_list.append(num)
        print(f"✅ 读取成功！共读取到 {len(result_list)} 条数据。")

    except FileNotFoundError:
        # 处理文件不存在的异常
        print(f"❌ 错误：找不到文件 {filename}！")
    except ValueError:
        # 处理文件内容不是数字的异常
        print("❌ 错误：文件里的内容不是合法的数字！")
    except Exception as e:
        print(f"❌ 未知错误：{e}")

    return result_list


# 3. 演示异常处理实战（防崩溃的输入）
def safe_input_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value  # 输入对了，把数字交出去并结束循环
        except ValueError:
            print("❌ 输入错误：必须输入数字！请重新输入。")


# ===== 主程序测试区 =====
print("=== 文件与异常处理综合测试 ===")

# 测试 1：安全的数字输入
print("\n【测试 1：防崩溃输入】")
num1 = safe_input_float("请输入一个数字：")
print(f"你输入的数字是：{num1}")

# 测试 2：保存数据
my_scores = [88, 95, 76, 92]
save_data_to_file("my_scores.txt", my_scores)

# 测试 3：读取数据
read_list = read_data_from_file("my_scores.txt")
print(f"读回来的列表内容是：{read_list}")

# 测试 4：读取一个不存在的文件（测试异常防弹衣）
read_data_from_file("no_such_file_123.txt")