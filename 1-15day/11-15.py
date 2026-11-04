# ==========================================
# 第 11-15 天终极复习：学生综合信息管理系统
# ==========================================
# 融合点：字典、函数封装、列表套字典、异常处理

# 【第14天：函数定义】
# 定义一个函数，用来计算字典列表里的平均分
def calculate_avg(students_list):
    if len(students_list) == 0:
        return 0
    total = 0
    for stu in students_list:
        total = total + stu["成绩"]  # 【第12天：字典取值】
    return total / len(students_list)


# 主程序开始
print("=== 欢迎来到学生信息管理系统 ===")
students = []  # 【第11天：列表套字典的雏形】

while True:
    print("\n" + "=" * 20)
    print("1. 添加学生信息")
    print("2. 查看所有学生")
    print("3. 计算班级平均分")
    print("4. 退出系统")
    print("=" * 20)

    choice = input("请选择操作（1-4）：")

    if choice == "1":
        # 【第15天：综合防错机制】
        name = input("请输入学生姓名：")

        while True:
            score_str = input("请输入学生成绩：")
            try:
                score = float(score_str)  # 【第3天：类型转换】
                break  # 成功转换就跳出循环
            except ValueError:  # 【第20天（预支）：异常处理】
                print("❌ 错误：成绩必须是数字，请重新输入！")

        # 【第12天：创建字典】
        student_dict = {"姓名": name, "成绩": score}

        # 【第11天：把字典存入列表】
        students.append(student_dict)
        print(f"✅ {name} 的信息添加成功！")

    elif choice == "2":
        if len(students) == 0:
            print("⚠️ 暂无学生数据。")
        else:
            print("\n--- 学生列表 ---")
            # 【第13天：遍历列表里的字典】
            for i in range(len(students)):
                stu = students[i]
                # 使用 .get() 安全取值
                s_name = stu.get("姓名", "未知")
                s_score = stu.get("成绩", "缺考")
                print(f"第 {i + 1} 名：{s_name}，成绩：{s_score}")

    elif choice == "3":
        # 【第14天：调用自定义函数】
        avg_score = calculate_avg(students)
        print(f"\n📊 当前共有 {len(students)} 名学生。")
        print(f"📊 班级平均分是：{avg_score:.2f}")

    elif choice == "4":
        print("👋 退出系统，再见！")
        break
    else:
        print("❌ 输入错误，请重新输入！")