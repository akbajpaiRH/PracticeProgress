from subprocess import Popen, PIPE

process = Popen(['cat', 'example.py'], stdout=PIPE, stderr=PIPE)

stdout, stderr = process.communicate()

print(process.returncode)
print(process.stderr)
print(process.pid)
print(stdout)
