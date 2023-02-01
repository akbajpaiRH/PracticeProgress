import subprocess

# command = ['spaship','init']

p = subprocess.Popen(["spaship", "init"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)

# inputs = [b'Akash\n', b'/\n', b'y\n']
# for input_ in inputs:
#     p.stdin.write(input_)
# p.stdin.close()
p.stdin.write(b'Akash\n')
p.stdin.write(b"/\n")
p.stdin.write(b"y\n")

output, error = p.communicate()

p.wait()
print(p.returncode)
print(output.decode())
# output = p.stdout
print(output)
print(len(output))
