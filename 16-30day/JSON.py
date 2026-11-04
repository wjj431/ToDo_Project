import json

print("=== 任务一:字典转JSON字符串 ===")
student={
    "姓名":"张三",
    "年龄":18,
    "成绩":[90,85,95],
    "是否毕业":False
}
json_str=json.dumps(student,ensure_ascii=False)
print("转换前的类型:",type(student))
print("转换后的类型:",type(json_str))
print("转换前的样子:",student)
print("转换后的样子:",json_str)

print("\n=== 任务二:JSON字符串转回字典 ===")
received_str='{"课程":"Python","难度":3}'
my_dict=json.loads(received_str)
print("转换前的类型:",type(received_str))
print("转换后的类型:",type(my_dict))
print("提取里面的课程:",my_dict["课程"])

print("\n=== 任务三:把字典存入JSON文件")
student_data={
    "班级":"人工智能三班",
    "学生":[
    {"姓名":"张三","成绩":95},
    {"姓名":"李四","成绩":88}
]
}
with open("student.json","w",encoding="utf-8") as f:
    json.dump(student_data,f,ensure_ascii=False,indent=4)
print("保存成功!去左边找找student.json打开看看")

print("\n=== 任务四:从JSON文件读回字典 ===")
with open("student.json","r",encoding="utf-8") as f:
    my_dict=json.load(f)
print("读回来的数据类型:",type(my_dict))
print("读回来的内容:",my_dict)
my_dict["学生"][0]["成绩"]=100
print("修改后张三的成绩:",my_dict["学生"][0]["成绩"])
