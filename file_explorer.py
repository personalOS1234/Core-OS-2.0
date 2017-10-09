# Created by Max Yurchenko on 07.10.2017
# email: joker0071911@gmail.com 
# feel free to ask any questions) 
# Copyright(C) 2017  

import os


class readfolder:
    """list of files from folder"""
    fl = True
    home_directory = 'C:/'

    def __init__(self, folder = home_directory):
        self.folder = folder

    def openfolder(self):
        _counter = 1
        try:
            files = os.listdir(self.folder)
        except OSError:
            self.folder = self.home_directory
            print('No such File or Diretrory, PRESS ENTER')
            input()
            return
        os.system('cls')
        print('Current Directory:', self.folder)
        for i in files:
            print(_counter, ' ', i)
            _counter += 1
        print('to open file print "file"')
        print('print "back"to go to the previous directory')
        self.newfolder = input('Input Folder Name("end to stop"): ')
        if self.newfolder == 'end':
            self.fl = False
        elif self.newfolder == 'back':
            self.folder = self.home_directory
            return
        self.folder = self.folder + '/' + self.newfolder

    def info_from_file(self, filename):
        _data = open(filename, 'r')
        data = _data.read()
        return data

    def write_in_file(self, filename, mode='a+', *args):
        _data = open(filename, mode=mode)
        _data.write(args)

