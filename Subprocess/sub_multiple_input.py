import subprocess

command = ['python', '-c', 'a=input(); b=input(); print(a+b)']

p = subprocess.run(command, stdout=subprocess.PIPE, input="Hello\n World\n", encoding='utf-8')

output = p.stdout
print(output)