import json,pickle,os

print('\nPart1-------------------')
d = dict(name = 'bob', age = 20, score = 88)
res = json.dumps(d)
print('res = ', res)
print('\nPart2-------------------')
json_string=json.dumps(d)
res2 = json.loads(json_string)
print('res = ', res2)

print('\nPart3-------------------')

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age  = age
        self.score= score
def student2dict(std):
    return{'name' : std.name,
           'age'  : std.age,
           'score': std.score
           }
s=Student('bob', 20, 88)
print('1:'+json.dumps(s, default=student2dict))
print('2:'+json.dumps(s, default=lambda obj:obj.__dict__))

print('\nPart4-------------------')

def dict2student(s):
    return Student(s['name'], s['age'], s['score'])

print(json.loads(json_string, object_hook=dict2student))


print('\nPart5-------------------')

s1 = json.dumps(json_string, ensure_ascii=False)
s2 = json.dumps(json_string, ensure_ascii=True)
print(s1+s2)


print('\nPart6-------------------')
a = os.path.abspath('.')
b = os.path.join(a, 'pickling_test')
c = os.path.join(b, 'pratice_review.txt')
fi = open(c, 'w')
std2 = Student('唐乖乖', 25, 99)
std_p = json.dump(std2, fi,default=lambda obj:obj.__dict__,ensure_ascii=True)
fi.close()
fi2 = open(c, 'r')
std_pp = json.load(fi2)
print(std_pp)