import subprocess

print('$ nslookup')
p = subprocess.Popen(['nslookup'],
                     stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')  # our,err这个没理解
print(output.decode('utf-8'))
print('Exit code:', p.returncode)