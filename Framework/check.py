import subprocess
import os
import time
from collections import Counter
import csv
import base64

secret = ""
with open('/home/akbajpai/PycharmProjects/pythonProject/Subprocess/DEMO/secret.txt', 'r') as f:
    line = f.readline()
    secret = base64.urlsafe_b64decode(line)


class Test:
    def create(self, str):
        try:
            p1 = subprocess.run(
                ['touch',
                 '/home/akbajpai/PycharmProjects/pythonProject/Subprocess/DEMO/{file_name}'.format(file_name=str)],
                stdout=subprocess.PIPE, encoding='utf-8')
            assert p1.returncode == 0
            return 1
        except Exception as e:
            print(e)

    def check(self, st, d):
        # print(os.getcwd())
        p1 = subprocess.run(['ls', '/home/akbajpai/PycharmProjects/pythonProject/Subprocess/DEMO/'], text=True,
                            stdout=subprocess.PIPE,
                            encoding='utf-8')
        assert p1.returncode == 0
        # print(p1.stdout)
        if st == 'junk.txt':
            print("inside if")
            # pswrd = "Akashbajpai$1226"
            pswrd = secret
            inp1 = subprocess.Popen(['echo', pswrd], stdout=subprocess.PIPE)
            inp2 = subprocess.Popen(["sudo", "-S", "chattr", "+i",
                                     "/home/akbajpai/PycharmProjects/pythonProject/Subprocess/DEMO/{file_name}".format(
                                         file_name=st)], stdin=inp1.stdout, stdout=subprocess.PIPE)
            out, err = inp2.communicate()

        if st in p1.stdout:
            try:
                cmd = "rm -f /home/akbajpai/PycharmProjects/pythonProject/Subprocess/DEMO/{file_name}"
                cmd = cmd.format(file_name=st)
                print(cmd)
                r = subprocess.run(cmd, shell=True)

                if r.returncode == 0:
                    d += 1

                p1 = subprocess.run(['ls', '/home/akbajpai/PycharmProjects/pythonProject/Subprocess/DEMO/'], text=True,
                                    stdout=subprocess.PIPE,
                                    encoding='utf-8')
                assert st not in p1.stdout
                return d
            except Exception as e:
                print("You don't have permission to delete the file")
                print(str(e))
                return d
        else:
            print("No file found")


obj = Test()
l = ['junk3.txt', 'junk2.txt', 'junk3.txt', 'junk4.txt', 'junk5.txt', 'junk8.txt', 'junk7.txt', 'junk5.txt']
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
    print(each)
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
