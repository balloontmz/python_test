from io import StringIO

f=StringIO('Hello\nhi!\ngood!')
print(f)

while True:
    s=f.readline()
    if s == '':
        break
    print(s.strip())