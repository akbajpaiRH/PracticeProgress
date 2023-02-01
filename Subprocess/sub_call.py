import subprocess
from subprocess import PIPE,Popen
# p=subprocess.call(["ls", "-l"])
pswrd = "Akashbajpai$1226"
p = Popen(['echo', pswrd], stdout=PIPE)
p1 = Popen(["sudo", "-S","ls", "-la"], stdin=p.stdout, stdout=PIPE)

# p1.stdin.write(b'Akashbajpai$1226\n')
stdout= p1.communicate()[0]
print(stdout.decode())
print(p1.returncode)