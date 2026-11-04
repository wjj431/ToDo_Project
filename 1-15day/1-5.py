# ==========================================
# 第 1-5 天终极复习：学生成绩管理与评级
# ==========================================

print("=== 欢迎来到成绩录入系统 ===")

# 【第2天：变量与字符串】接收用户名字
student_name = input("请输入学生的姓名：")

# 【第5天：列表】准备一个空列表，用来存成绩
scores = []

# 【第1天、第3天：输入与格式化】录入成绩
print(f"\n开始录入 {student_name} 的成绩：")

# 成绩1
score1 = float(input("请输入第1门成绩（0-100）："))
scores.append(score1) # 【第5天：append 追加】

# 成绩2
score2 = float(input("请输入第2门成绩（0-100）："))
scores.append(score2)

# 成绩3
score3 = float(input("请输入第3门成绩（0-100）："))
scores.append(score3)

# 【第5天：列表切片与索引】
print(f"\n你录入的所有成绩是：{scores}")
print(f"第一门成绩是：{scores[0]}")
print(f"最后一门成绩是：{scores[-1]}")

# 【第2天：数学运算】计算总和与平均值
total = score1 + score2 + score3
average = total / 3

print(f"总分是：{total}")
# 【第3天：f-string 格式化】保留2位小数
print(f"平均分是：{average:.2f}")

# 【第4天：条件判断】根据平均分给出评级
print("\n=== 成绩评级 ===")
if average >= 90:
    print("🏆 评级：A（优秀）")
elif average >= 80:
    print("🌟 评级：B（良好）")
elif average >= 70:
    print("👍 评级：C（中等）")
elif average >= 60:
    print("😐 评级：D（及格）")
else:
    print("💥 评级：F（不及格，需要补考！）")

# 【第5天：列表操作】修改和删除
print("\n=== 列表操作演示 ===")
scores.remove(score3) # 删掉第3门成绩
print(f"删除最后一门成绩后，列表变成了：{scores}")

scores.insert(0, 99.5) # 在第一个位置插入一个新成绩
print(f"在开头插入一个99.5后，列表变成了：{scores}")

print("\n=== 程序结束 ===")