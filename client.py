'''
#==============================================================================================#
# Pyhtos top level client interface:
##  Back-end, CLI interface


This is the higest level client interface meaning that there may be more features 
buried deeper in the repository. Each level may have a client module. This is 
not always the case. good luck ~jpd
#==============================================================================================#
'''

from modules import menu 
from modules.ntwrk import tpls_server
from node_server import NodeServer
from modules.chain import ipfs

from time import sleep
import os


login = False
run = True
titlestat = [0]

#==============================================================================================#
#### Classes
class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class DateTime():
    def dt(self):
        import datetime
        return datetime.datetime.now()

#define the class instances
admin1 = Admin('admin', 'password')
# hint: this line 
dt1 = DateTime()



#==============================================================================================#

def help_menu():
    '''
    TODO: Add more sarcastic comments for laughs.
    '''
    print(
        """
        _______HELP_PAGE_______
        =======================
        
        have you even read the source code? 
        
        did you actually read it though?

        seriously read the source for documentation though
        
        the best help is the help you give yourself.
        

        for root, dirs, files in os.walk(".", topdown=True):
            for file in files:
                print(os.path.join(root, file))

            for name in dirs:
                print(os.path.join(root, name))

        for dir in dirs:
            dirpath = os.path.join(root, dir)
            dirsize = os.path.getsize(dirpath)
            print(index, '\t\t', dirsize, '\t\t', dirpath)
            index += 1
        """
    )
    input('> ')

#==============================================================================================#
def title():
    # running titlebar
    print('=' * 80)
    print('PYTHOS\t\t\t\t\t', dt1.dt())
    #print('=' * 80)
    
    # subtitle
    if titlestat[0] == 0:
        print('\n\t\tLOGIN')
        print('=' * 80)
    
    elif titlestat[0] == 1:
        print('\n\t\tLOGIN FAILED')
        print('=' * 80)
    
    elif titlestat[0] == 2:
        print('\n\t\tNODE_ADMIN')
        print('=' * 80)

def clear():
    import platform
    ops = platform.system()
    if ops == 'Darwin':
        os.system('clear')
    else:
        os.system('cls')

def refresh_screen():
    clear()
    title()


#==============================================================================================#
####### LOGIN SEQUENCE #######

if login == False:
    titlestat.clear()
    titlestat.append(2)

while login:
    #title()
    usn = input('username: ')
    if usn != admin1.username:
        titlestat.clear()
        titlestat.append(1)
        refresh_screen()
                
    elif usn == admin1.username:
        titlestat.clear()
        titlestat.append(0)
        refresh_screen()
        pasw = input('password: ')

        if pasw == admin1.password:
            titlestat.clear()
            titlestat.append(2)
            refresh_screen()
            print('You are logging in as ', usn)
            refresh_screen()
            break
#==============================================================================================#


#==============================================================================================#
def rfsm():
    path = input('path>')
    p = rfs(path)
    print(p)

def rfs(pathname):
    
    index = 0
    tsizevar = 0
    print('\n\nINDEX\t\tSIZE\t\tDIRECTORY')
    print('=' * 80)
    for root, dirs, files in os.walk(pathname):
        for file in files:
            try:
                try:
                    pathname = os.path.join(root, file)
                    size = os.path.getsize(pathname)
                    tsizevar += size
                    print(index, '\t\t', size, '\t\t', pathname)
                    index += 1
                except PermissionError:
                    print('perm error')

            except (FileNotFoundError, OSError):
                print('file not found error')

    returndata = {'indexed files': index,'totalsize': tsizevar}
    print(returndata)
    input('>')
    return returndata

def rootfile_list_2():
    p = rfs('.')
    print(p)

def __setup():
    from setup import UserBuild
    ub = UserBuild()
    input('>>')

def __tpls_server():
    __node = NodeServer('cfg.txt')
    ing = input(">>")

def __ntwrk_menu():
    menu.initialize_menu(networking_menu_dict, "NETWORKING MAIN MENU")

def __ipfs_write():
    ipfs.IPFS_add_file('cfg.txt')
    input('>')


# Main menu dictionary
mm = {
    'current directory info': rootfile_list_2,
    'custom directory info': rfsm,
    'setup': __setup,
    'networking menu': __ntwrk_menu
}

networking_menu_dict = {
    'functional tpls_server': __tpls_server,
    'write to ipfs': __ipfs_write

}

#==============================================================================================#
######## APP INTERFACE ########
while run:
    refresh_screen()
    command = input('>')
    if command == '0':
        refresh_screen()
        print('LOGING OUT OF THE MATRIX')
        clear()
        break
    
    elif command == "help":
        refresh_screen()
        help_menu()

    elif command == '1':
        refresh_screen()              
        menu.initialize_menu(mm, 'PYTHOS MAIN MENU')

    elif command == '2':
        refresh_screen()
        __ntwrk_menu()
    

#==============================================================================================#
