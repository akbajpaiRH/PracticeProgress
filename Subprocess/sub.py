from subprocess import Popen, PIPE

process = Popen(['cat', 'example.py'], stdout=PIPE, stderr=PIPE)

stdout, stderr = process.communicate()

print(stdout)
