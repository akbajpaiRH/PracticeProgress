import subprocess
import os
import time
from collections import Counter
import csv


class Test:
    def create(self, str):
        try:
            p1 = subprocess.run(
                ['touch',
                 '/home/akbajpai/PycharmProjects/pythonProject/Subprocess/DEMO/{file_name}'.format(file_name=str)],
                stdout=subprocess.PIPE, encoding='utf-8')
            return 1
        except:
            print("File with same name exits")

    def check(self, st, d):
        # print(os.getcwd())
        p1 = subprocess.run(['ls', '/home/akbajpai/PycharmProjects/pythonProject/Subprocess/DEMO/'], text=True,
                            stdout=subprocess.PIPE,
                            encoding='utf-8')
        if st in p1.stdout:
            print("-------------FOUND------------------" + st)
            try:
                subprocess.call(['rm', '/home/akbajpai/PycharmProjects/pythonProject/Subprocess/DEMO/{}'.format(st)])
                d += 1
                p1 = subprocess.run(['ls', '/home/akbajpai/PycharmProjects/pythonProject/Subprocess/DEMO/'], text=True,
                                    stdout=subprocess.PIPE,
                                    encoding='utf-8')
                assert st not in p1.stdout
                return d
            except:
                print("You don't have permission to delete the file")
        else:
            print("No file found")


obj = Test()
l = ['junk.txt', 'junk2.txt', 'junk3.txt','junk4.txt','junk5.txt','junk.txt','junk7.txt','junk5.txt']
c = len(l)
l1 = set(l)
print(c)

i = 0
for each in l1:
    i += obj.create(each)
print(i)

# time.sleep(2)

d = 0
for each in l1:
    d = obj.check(each, d)
print(d)

filename = "data.csv"
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Total inputs passed', str(c)])
    csvwriter.writerow(['files created', str(i)])
    csvwriter.writerow(['files deleted', str(d)])
    if (i != d):
        csvwriter.writerow(['files not deleted', str(i - d)])
