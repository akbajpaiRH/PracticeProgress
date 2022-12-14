import subprocess

s = subprocess.check_output(["pytest", "-v"], encoding='utf-8')
assert "2 passed" in s
assert "failed" not in s
print(s)
