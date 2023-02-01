import subprocess

inputs = [b"Akash\n", b"1.0.0\n", b"This is a random project\n", b"\n", b"\n", b"\n", b"\n", b"Akash\n", b"3.1.2\n",b"\n"]

p = subprocess.Popen(["npm", "init"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
p.stdin.write(b"Akash\n")
p.stdin.write(b"1.0.0\n")
p.stdin.write(b"tefcdQQDqed\n")
p.stdin.write(b"\n")
p.stdin.write(b"\n")
p.stdin.write(b"\n")
p.stdin.write(b"\n")
p.stdin.write(b"Akash\n")
p.stdin.write(b"3.1.2\n")
p.stdin.write(b"y\n")
# for input_ in inputs:
#     p.stdin.write(input_)
# p.stdin.close()
output, error = p.communicate()
print(p.returncode)
# p = subprocess.Popen(["npm", "init", "-y"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
# out, err = p.communicate()
# print(p.returncode)
