import subprocess
with open('example.txt', 'w') as f:
    p1=subprocess.run(['ls','-la','../../'],stdout=f,encoding='utf-8')


