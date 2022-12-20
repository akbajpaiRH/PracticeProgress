import subprocess

p1=subprocess.run(['cat','test.txt'],stdout=subprocess.PIPE,text=True)
print(p1.returncode)
print(p1.stdout)

print("-----------------------------------------------------------------")

p2=subprocess.run(['grep','-n','and'],stdout=subprocess.PIPE,input=p1.stdout,text=True)
print(p2.returncode)
print(p2.stdout)