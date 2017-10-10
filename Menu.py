# Created by Max Yurchenko on 09.10.2017
# email: joker0071911@gmail.com 
# feel free to ask any questions) 
# Copyright(C) 2017  

from commonFunctions import *

def menu_work(MenuObject, menu_name):
    menu_points = MenuObject.get_menu_points(menu_name)
    if exception_checking(menu_points):
        return Exception
    for i in range(len(menu_points)):
        print(str(i+1)+' '+menu_points[i])
    choice = int(input('Input your choice: '))
    return choice-1

class Menu:
    def __init__(self):
        menu_file = open('os_data/menu.data')
        menu_data = menu_file.read()
        menu_data = menu_data.split(';')
        menu_data.remove(menu_data[len(menu_data) - 1])
        self.buf = menu_data
        self.menu_data = {}
        for i in menu_data:
            menu_name, menu = i.split(':')
            self.menu_data[menu_name] = menu
        for i in self.menu_data.keys():
            self.menu_data[i] = self.menu_data[i].split()

    def get_menu_points(self, menu_name):
        menu_points = self.menu_data[menu_name]
        if not menu_points:
            return Exception
        else:
            return menu_points


a=Menu()
b = menu_work(a,'main')
print(b)