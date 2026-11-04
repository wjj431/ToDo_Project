# ==========================================
# 第 6-10 天终极复习：智能成绩管理系统
# ==========================================
import random  # 【第9天：导入随机数模块】

print("=== 欢迎来到智能成绩管理系统 ===")

while True:  # 【第7天：while 循环控制主菜单】
    print("\n" + "=" * 20)
    print("1. 批量录入成绩并分析")
    print("2. 玩个猜数字游戏")
    print("3. 打印星号直角三角形")
    print("4. 退出系统")
    print("=" * 20)

    choice = input("请选择操作（1-4）：")

    if choice == "1":
        # 【第10天：综合系统，结合第6天的找最大值】
        print("\n--- 成绩分析模式 ---")
        scores = []

        # 【第7天：for循环】固定录入5个成绩
        for i in range(5):
            score = float(input(f"请输入第 {i + 1} 个成绩："))
            scores.append(score)

        # 【第6天：禁用max/min，自己写打擂台逻辑】
        max_val = scores[0]
        min_val = scores[0]
        total = 0

        # 【第7天：遍历列表】
        for s in scores:
            total = total + s
            if s > max_val:
                max_val = s
            if s < min_val:
                min_val = s

        avg = total / len(scores)

        print(f"\n✅ 分析完成：")
        print(f"最高分：{max_val}，最低分：{min_val}，平均分：{avg:.2f}")

    elif choice == "2":
        # 【第9天：猜数字游戏】
        print("\n--- 猜数字游戏（1-100） ---")
        target = random.randint(1, 100)
        count = 0

        while True:
            guess = int(input("请输入你猜的数字："))
            count = count + 1

            if guess == target:
                print(f"🎉 猜对了！你用了 {count} 次。")
                break
            elif guess > target:
                print("大了！")
            else:
                print("小了！")

    elif choice == "3":
        # 【第8天：嵌套循环打印图形】
        print("\n--- 打印直角三角形 ---")
        # 用两层循环实现（不用字符串乘法）
        for i in range(1, 6):  # 外层控制行数
            for j in range(i):  # 内层控制每行的星号数
                print("*", end="")  # 不换行打印
            print()  # 每行打完换行

    elif choice == "4":
        print("👋 退出系统，再见！")
        break  # 【第7天：break 退出死循环】

    else:
        print("❌ 输入错误，请重新选择！")