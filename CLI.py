import subprocess
import os

print(os.getcwd())

os.chdir(os.getcwd())

s = subprocess.check_output(["pytest", "-v"], encoding='utf-8')
# s2 = subprocess.check_output(["ls"], encoding='utf-8')
# print(s)
# print(s.returncode)
num = 0
temp = s.split("\n")
for line in temp:
    if line.startswith("collecting"):
        # print(line)
        num = line.split(" ")[3]
        # print(num)
        # print(type(num))

assert "platform linux" in s
assert "Python 3.9.13" in s
assert "pytest-7.2.0" in s
assert "pluggy-1.0.0" in s
assert num + " passed" in s
assert "failed" in s
