import subprocess
import os


class est:
    def check(self):
        # print(os.getcwd())
        p1 = subprocess.check_output(['ls', '/home/akbajpai/PycharmProjects/pythonProject/Subprocess/DEMO/'],
                                     encoding='utf-8')
        if 'junk.txt' in p1:
            print("-------------FOUND------------------")
            subprocess.call(['rm', '/home/akbajpai/PycharmProjects/pythonProject/Subprocess/DEMO/junk.txt'])
            p1 = subprocess.check_output(['ls', '/home/akbajpai/PycharmProjects/pythonProject/Subprocess/DEMO/'],
                                         encoding='utf-8')
            if 'junk.txt' in p1:
                print("You dont have the permission to delete that file")
            else:
                print("File deleted successfully")
        else:
            print("no file found")

obj = est()
obj.check()
