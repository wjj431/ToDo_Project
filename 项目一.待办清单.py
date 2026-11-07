import json
import os

# 数据文件路径
FILE_NAME = "tasks.json"

# ==========================================
# 1. 核心功能函数
# ==========================================
def load_tasks():
    """读取本地 JSON 数据"""
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_tasks(tasks):
    """保存数据到本地 JSON"""
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)

def show_menu():
    """显示菜单"""
    print("\n" + "="*20)
    print("1. 添加待办")
    print("2. 查看全部")
    print("3. 标记完成")
    print("4. 删除")
    print("5. 退出")
    print("="*20)

# ==========================================
# 2. 主程序逻辑
# ==========================================
def main():
    print("=== 欢迎使用待办清单系统 ===")
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("请选择操作（1-5）：")

        if choice == "1":
            task_content = input("请输入待办事项的内容：")
            task_id = 1 if len(tasks) == 0 else tasks[-1]["id"] + 1
            new_task = {"id": task_id, "内容": task_content, "是否完成": False}
            tasks.append(new_task)
            save_tasks(tasks)
            print(f"添加成功！当前共有 {len(tasks)} 个待办。")

        elif choice == "2":
            if len(tasks) == 0:
                print("⚠️ 当前没有待办事项。")
            else:
                print("\n--- 待办列表 ---")
                for t in tasks:
                    status = "[x]" if t["是否完成"] else "[ ]"
                    print(f"{status} ID:{t['id']} - {t['内容']}")

        elif choice == "3":
            if len(tasks) == 0:
                print("⚠️ 当前没有待办事项。")
            else:
                task_id_str = input("请输入要标记完成的 ID：")
                try:
                    target_id = int(task_id_str)
                    found = False
                    for t in tasks:
                        if t["id"] == target_id:
                            t["是否完成"] = True
                            save_tasks(tasks)
                            print(f"ID {target_id} 已标记为完成！")
                            found = True
                            break
                    if not found:
                        print("错误：找不到这个 ID！")
                except ValueError:
                    print("错误：ID 必须是数字！")

        elif choice == "4":
            if len(tasks) == 0:
                print("⚠️ 当前没有待办事项。")
            else:
                task_id_str = input("请输入要删除的 ID：")
                try:
                    target_id = int(task_id_str)
                    found = False
                    for i in range(len(tasks)):
                        if tasks[i]["id"] == target_id:
                            del tasks[i]
                            save_tasks(tasks)
                            print(f"ID {target_id} 已删除！")
                            found = True
                            break
                    if not found:
                        print("错误：找不到这个 ID！")
                except ValueError:
                    print("错误：ID 必须是数字！")

        elif choice == "5":
            print("退出系统。")
            break
        else:
            print("⚠️ 输入错误，请重新选择。")

# 程序入口
if __name__ == "__main__":
    main()