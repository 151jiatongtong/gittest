import json

all_record = []
id_record = 0
dic = {}

def add_record():
    name = input("请输入姓名：")
    phone = input("请输入电话：")
    dic["name"] = name
    dic["phone"] = phone

    print("添加成功：", dic)

def query_record():
    name = input("请输入姓名：")
    with open("record.txt", "r") as f:
        for i in json.loads(f.read()):
            if name == i.get("name"):
                print(i)


def change_record():
    old = input("请输入要修改人姓名：")
    change = int(input("请选择要修改的信息：1.name 2.phone"))
    new = input("请输入新的name 或 phone")
    with open("record.txt", "r") as f:
        for i in json.loads(f.read()):
            if old == i.get("name"):
                if change == 1:
                    i["name"] = new
                else:
                    i["phone"] = new
    print("修改成功")

def delete_record():
    name = input("请输入name：")
    with open("record.txt", "r") as f:
        for i in json.loads(f.read()):
            if name == i["name"]:
                newlist = json.loads(f.read()).remove(i)
                with open("record.txt", "w") as f:
                    f.write(json.dumps(newlist))
    print("删除成功")

add_record()

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

# main()
