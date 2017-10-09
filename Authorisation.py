# Created by Max Yurchenko on 07.10.2017
# email: joker0071911@gmail.com 
# feel free to ask any questions) 
# Copyright(C) 2017  

from crypto import *
from commonFunctions import *
import os


class Authorisation:

    users = {}
    def __init__(self):
        printOSinfo()
        input()
        self.parse_user_data_file()
        self.login = input('Input login: ')
        if self.login == 'reg':
            self.reg()
        else:
            self.password = input('Input password: ')
            try:
                if self.password == self.users[self.login]:
                    self.successful_login = True
            except Exception as e:
                print('error')
                self.successful_login = False

    def parse_user_data_file(self):
        user_data_file = open('os_data/users.dat')
        file_data = user_data_file.read()
        if not file_data:
            return
        file_data= file_data.split(';')
        file_data.remove(file_data[len(file_data)-1]) #empty element, i dunno why))
        for i in file_data:
            login, password = i.split(':')
            self.users[login] = password

    def reg(self):
        clear_screen()
        self.login = input('Input new login')
        if self.login in self.users.keys():
            print('User already exists')
            return -1
        self.password = input('Input password: ')
        conf_password = input('Confirm password: ')
        if not self.password == conf_password:
            print('Error.')
            input()
            return -1
        os.makedirs('user_data/'+self.login)
        user_data_file = open('os_data/users.dat','a')
        user_data_file.write(''+self.login+':'+self.password+';')

