#!/usr/bin/env python
# -*- coding: utf-8 -*-
import openpyxl
class Record:
    glo_id = 0

    def __init__(self, name, phone):
        self.glo_id += 1
        self.name = name
        self.phone = phone
        self.id = self.glo_id

    def set_number(self, phone):
        self.phone = phone

    def __str__(self):
        return "{}\t{}\t{}".format(self.glo_id, self.name, self.phone)


class PhoneBook:
    def __init__(self):
        self.data = []

    def add_record(self, record):
        self.data.append(record)

    def query_record(self, name):
        for da in self.data:
            if da.name == name:
                print("查询结果", da)

    def change_record(self, name):
        for i in self.data:
            if i.name == name:
                newphone = input("请输入要修改的电话：")
                i.set_number(newphone)
            else:
                print("修改失败")

    def delete_record(self, name):
        for de in self.data:
            if de.name == name:
                self.data.remove(de)
                print("删除成功：", de)
            else:
                print("不存在")
        pass


if __name__ == "__main__":
    phonebook = PhoneBook()
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
        if num in [1, 2, 3, 4, 5]:

            if num == 1:
                name = input("请输入姓名：")
                phone = input("请输入电话：")
                record = Record(name, phone)
                phonebook.add_record(record)
            if num == 2:
                name = input("请输入姓名：")
                phonebook.query_record(name)
            if num == 3:
                name = input("请输入姓名")
                phonebook.delete_record(name)
            if num == 4:
                name = input("请输入姓名")
                phonebook.change_record(name)
            if num == 5:
                print("退出")
                break
        else:
            print("无操作项")
            continue