import json
print("=== 欢迎使用待办清单系统 ===")
try:
    with open("tasks.json","r",encoding="utf-8") as f:
        tasks=json.load(f)
except FileNotFoundError:
    tasks=[]

tasks=[]
while True:
    print("\n"+"="*20)
    print("1.添加待办")
    print("2.查看全部")
    print("3.标记完成")
    print("4.删除")
    print("5.退出")
    print("="*20)
    choice=input("请选择操作(1-5):")
    if choice=="1":
        task_content=input("请输入待办事项的内容:")
        if len(tasks)==0:
            task_id=1
        else:
            task_id=tasks[-1]["id"]+1
        new_task={
            "id":task_id,
            "内容":task_content,
            "是否完成":False
        }
        tasks.append(new_task)
        print(f"添加成功!当前共有{len(tasks)}个待办")
    elif choice=="2":
        if len(tasks)==0:
            print("当前没有待办事项")
        else:
            print("\n--- 代办列表 ---")
            for t in tasks:
                if t["是否完成"]:
                    status="[x]"
                else:
                    status="[ ]"
                print(f"{status}ID:{t['id']}-{t['内容']}")
    elif choice=="3":
        if len(tasks)==0:
            print("当前没有待办事项")
        else:
            task_id_str=input("请输入要标记完成的ID:")
            try:
                task_id=int(task_id_str)
                found=False
                for t in tasks:
                    if t["id"] == task_id:
                        t["是否完成"]=True
                        print(f"ID{target_id}已标记为完成!")
                        found=True
                        break
                if not found:
                    print("错误:找不到这个ID!")
            except ValueError:
                print("错误:ID必须是数字!")
    elif choice=="4":
        if len(tasks)==0:
            print("当前没有待办事项")
        else:
            task_id_str=input("请输入要删除的ID:")
            try:
                target_id=int(task_id_str)
                found=False
                for i in range(len(tasks)):
                    if tasks[i]["id"] == target_id:
                        del tasks[i]
                        print(f"ID{target_id}已删除!")
                        found=True
                        break
                if not found:
                    print("错误:找不到这个ID!")
            except ValueError:
                print("错误:ID必须是数字!")
    elif choice=="5":
        print("退出系统.")
        break
    else:
        print("输入错误,请重新选择")
    if choice in ["1","3","4"]:
        with open("tasks.json","w",encoding="utf-8") as f:
            json.dump(tasks,f,ensure_ascii=False,indent=4)