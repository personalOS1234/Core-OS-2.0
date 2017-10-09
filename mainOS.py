# Created by Max Yurchenko on 07.10.2017
# email: joker0071911@gmail.com 
# feel free to ask any questions) 
# Copyright(C) 2017  

from Core import Core
import queue, os
from Authorisation import Authorisation
from commonFunctions import *

def main():
    clear_screen()
    auth = Authorisation()
    if not auth.successful_login:
        clear_screen()
        printOSinfo()
        print('Error. Try again.')
        return -1

if __name__ == '__main__':
    main()

