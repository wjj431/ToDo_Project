# ==========================================
# 第 16-17 天：函数进阶与作用域
# ==========================================

# 【全局变量】
global_score_limit = 100  # 这是一个全局变量，函数里面也能看到


# 1. 默认参数 + 多返回值 + 作用域
def analyze_scores(scores, show_detail=True):
    # scores 和 show_detail 是局部变量
    if len(scores) == 0:
        return 0, 0, 0  # 多返回值：空列表返回三个0

    max_val = max(scores)
    min_val = min(scores)
    avg_val = sum(scores) / len(scores)

    # 使用了全局变量 global_score_limit
    if max_val > global_score_limit:
        print("⚠️ 警告：发现了超过满分的异常成绩！")

    # 默认参数生效：如果外面没传 show_detail=False，这里就会打印
    if show_detail:
        print(f"【详情】最高分：{max_val}，最低分：{min_val}，平均分：{avg_val:.2f}")

    # 【核心】同时返回三个值，外面可以用三个变量接住
    return max_val, min_val, avg_val


# 2. 演示 global 关键字（修改全局变量）
def reset_limit():
    global global_score_limit  # 声明要修改外面的全局变量
    global_score_limit = 150  # 成功修改
    print(f"【函数内】满分限制被改成了：{global_score_limit}")


# ===== 主程序测试区 =====
print("--- 测试函数进阶 ---")
my_scores = [85, 90, 78, 60]

# 测试默认参数（不传第二个参数，它会自动打印详情）
print("1. 默认调用：")
max_num, min_num, avg_num = analyze_scores(my_scores)  # 多返回值接包

# 测试关键字参数（指名道姓地传）
print("\n2. 使用关键字参数关闭详情：")
analyze_scores(scores=my_scores, show_detail=False)

print("\n--- 测试 global 修改全局变量 ---")
print(f"【修改前】外部看到的限制是：{global_score_limit}")
reset_limit()
print(f"【修改后】外部看到的限制是：{global_score_limit}")