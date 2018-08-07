import json
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score =score

def student2dict(std):
    return {'name' : std.name,
            'age'  : std.age,
            'score': std.score
            }

Std1=Student('bob',20,88)
print(json.dumps(Std1,default=student2dict))
print('10086'+json.dumps(Std1,default=lambda obj:obj.__dict__))
zzz=json.dumps(Std1,default=student2dict)
def dict2student(d):
    return Student(d['name'],d['age'],d['score'])
print(json.loads(zzz, object_hook=dict2student))
print('10000')
