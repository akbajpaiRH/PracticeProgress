import subprocess

s = subprocess.check_output(["ls", "-la"], encoding='utf-8')

print(str(s))
print(type(s))
