import subprocess
import os
import time
from collections import Counter
import csv
import base64

path = '/home/akbajpai/PycharmProjects/pythonProject/Subprocess/DEMO/'
secret = ""
with open(path + 'secret.txt', 'r') as f:
    line = f.readline()
    secret = base64.urlsafe_b64decode(line)


class Test:
    def __init__(self):
        self.isImmutable = False

    def create(self, str):
        flag = False
        try:
            p1 = subprocess.run(
                ['touch',
                 path + '{file_name}'.format(file_name=str)],
                stdout=subprocess.PIPE, encoding='utf-8')
            if(p1.returncode!=0):
                raise Exception("File already exists")
            if str == 'junk.txt':
                self.isImmutable = True
                pswrd = secret
                inp1 = subprocess.Popen(['echo', pswrd], stdout=subprocess.PIPE)
                inp2 = subprocess.Popen(["sudo", "-S", "chattr", "+i",
                                         path + "/{file_name}".format(
                                             file_name=str)], stdin=inp1.stdout, stdout=subprocess.PIPE)
                out, err = inp2.communicate()
            return 1, p1.returncode
        except Exception as e:
            print(e)

    def check(self, st, d):
        flag = False
        p1 = subprocess.run(['ls', path],
                            stdout=subprocess.PIPE,
                            encoding='utf-8')

        if st in p1.stdout:
            try:
                cmd = "rm -f {path}{file_name}"
                cmd = cmd.format(path=path, file_name=st)
                r = subprocess.run(cmd, shell=True)
                if r.returncode == 0:
                    flag = True
                    d += 1

                if flag == False:
                    print("You don't have delete permission")
                p1 = subprocess.run(['ls', path],
                                    stdout=subprocess.PIPE,
                                    encoding='utf-8')
                return d, p1.stdout, r.returncode, flag
            except Exception as e:
                print(str(e))
                return d
        else:
            print("No file found")
            return d, p1.stdout, 0, flag


obj = Test()
l = ['junk9.txt', 'junk2.txt', 'junk3.txt', 'junk4.txt', 'junk5.txt', 'junk8.txt', 'junk7.txt', 'junk5.txt']
c = len(l)
l1 = set(l)
print(c)

i = 0
for each in l1:
    res = obj.create(each)
    i += res[0]
print(i)

# time.sleep(2)

d = 0
for each in l1:
    res = obj.check(each, d)
    d = res[0]
print(d)

filename = "data.csv"
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Total inputs passed', str(c)])
    csvwriter.writerow(['files created', str(i)])
    csvwriter.writerow(['files deleted', str(d)])
    if i != d:
        csvwriter.writerow(['files not deleted', str(i - d)])
