# -*- coding: utf-8 -*-

# 使用dict实现学生成绩表，并提供增删改查功能

print("\n``````欢迎进入学生成绩信息数据管理中心！``````\n")
MENU = ("1.录入", "2.查询", "3.修改", "4.删除", "5.预览", "6.退出")
menus = ""
for menu in MENU:
    menus += (menu + "\t")
students = {}
MENU_NUMBERS = ("1", "2", "3", "4", "5", "6")
isExit = False
option = 0
while not isExit:
    inputKey = ""
    if 6 > option > 0:
        key = input("是否要继续（任意键返回主菜单，Y继续）：")
        if key == "Y" or key == "y":
            inputKey = str(option)
        else:
            option = 0
            continue
    else:
        print(menus)
        inputKey = input("请输入您要操作的菜单序号：")
    if inputKey in MENU_NUMBERS:
        isExit = (int(inputKey) == 6)
        if isExit:
            print("您已退出本次使用！")
        while int(inputKey) == 1:
            name = input("\t请输入学生姓名：")
            result = input("\t请输入%s的成绩：" % name)
            students[name] = result
            option = 1
            break
        while int(inputKey) == 2:
            CHILD_MENUS = ("1.学生查询", "2.平均成绩", "3.统计排名", "4.返回上一级")
            CHILD_MENUS_NUMBERS = ("1", "2", "3", "4")
            print(CHILD_MENUS)
            inputNum = input("\t请输入要查询的菜单序号：")
            if inputNum in CHILD_MENUS_NUMBERS:
                if int(inputNum) == 4:
                    break
                while int(inputNum) == 1:
                    name = input("\t请输入您要查询的学生姓名：")
                    if not name in students:
                        print("******系统没有找到姓名为%s的学生信息" % name)
                    else:
                        print("\t学生%s的成绩为%s" % (name, students[name]))
                    break
                while int(inputNum) == 2:
                    avgnum = 0
                    for value in students.values():
                        avgnum += int(value)
                    count = len(students)
                    print("共%d个学生，平均成绩为：%.2f" % (count, avgnum / float(count)))
                    break
                while int(inputNum) == 3:
                    r = sorted(students.items(), key=lambda x: x[1], reverse=True)
                    print("\t姓名\t\t成绩")
                    for key, value in r:
                        print("\t%s\t\t%s" % (key, value))
                    break
            option = 2
            break
        while int(inputKey) == 3:
            name = input("\t请输入您要修改的学生姓名：")
            if not name in students:
                print("******系统没有找到姓名为%s的学生信息" % name)
            else:
                result = input("\t请输入%s的新成绩：" % name)
                students[name] = result
            option = 3
            break
        while int(inputKey) == 4:
            name = input("\t请输入您要删除的学生姓名：")
            if not name in students:
                print("******系统没有找到姓名为%s的学生信息" % name)
            else:
                students.pop(name)
            option = 4
            break
        while int(inputKey) == 5:
            if len(students) == 0:
                print("******当前数据中心没有任何信息可供查询！")
                break
            print("\t姓名\t\t成绩")
            for key, value in students.items():
                print("\t%s\t\t%s" % (key, value))
            option = 5
            break