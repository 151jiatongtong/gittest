
all_record = []
id_record = 0


def add_record():
    name = input("请输入姓名：")
    phone = input("请输入电话：")
    global id_record
    id_record += 1
    dic = {}
    dic["name"] = name
    dic["phone"] = phone
    dic["id"] = id_record
    all_record.append(dic)
    print("添加成功：", dic)
    return all_record



def query_record():
    name = input("请输入姓名：")
    for listname in all_record:
        if listname["name"] == name:
            print("查询结果：", listname)
        else:
            print("查询失败")

def change_record():
    old = input("请输入要修改人姓名：")
    change = int(input("请选择要修改的信息：1.name 2.phone:"))
    new = input("请输入新的name 或 phone:")
    for i in all_record:
        if old == i.get("name"):
            if change == 1:
                i["name"] = new
            else:
                i["phone"] = new
        else:
            print("姓名不存在")
    print("修改成功")

def delete_record():
    name = input("请输入name：")
    for i in all_record:
        if name == i["name"]:
            all_record.remove(i)
            print("删除成功：", all_record)
        else:
            print("删除失败")



def main():
    while True:
        print(
            "通讯录: \n"
            "1. 添加 \n"
            "2. 查找 \n"
            "3. 删除 \n"
            "4. 修改 \n"
            "5. 退出 \n"
        )
        num = int(input("请选择操作："))

        if num == 1:
            add_record()
        if num == 2:
            query_record()
        if num == 3:
            delete_record()
        if num == 4:
            change_record()
        if num == 5:
            print("退出")
            break

if __name__ == "__main__":
    main()
