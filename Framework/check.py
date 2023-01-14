import subprocess
import os
import time


class Test:
    def create(self,str):
        # print(os.getcwd())
        # print(str)
        cmd = 'touch /home/akbajpai/PycharmProjects/pythonProject/Subprocess/DEMO/{file_name}'
        cmd = cmd.format(file_name=str)
        print(cmd)
        p1=subprocess.Popen([cmd], shell=True, encoding='utf-8')
        # p1=subprocess.Popen(['touch','./Subprocess/DEMO/',str],encoding='utf-8')
    def check(self,st):
        # print(os.getcwd())
        p1 = subprocess.check_output(['ls', '/home/akbajpai/PycharmProjects/pythonProject/Subprocess/DEMO/'],
                                     encoding='utf-8')
        if st in p1:
            print("-------------FOUND------------------"+st)
            subprocess.call(['rm', '/home/akbajpai/PycharmProjects/pythonProject/Subprocess/DEMO/{}'.format(st)])
            p1 = subprocess.check_output(['ls', '/home/akbajpai/PycharmProjects/pythonProject/Subprocess/DEMO/'],
                                         encoding='utf-8')
            if st in p1:
                print("You dont have the permission to delete that file")
            else:
                print("File "+st+" deleted successfully")
        else:
            print("No file found")

obj = Test()
l=['junk.txt','junk2.txt','junk3.txt']
for each in l:
    obj.create(each)

# time.sleep(2)

for each in l:
    obj.check(each)

# print(str(c)+" files found and "+str(d)+" files deleted")