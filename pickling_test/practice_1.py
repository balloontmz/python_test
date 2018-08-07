import json,pickle

# from the review area
print('\nPart1')
d = dict(name = 'Bob', age = 20, score = 88)
res = json.dumps(d)
print('res = ', res)
print('\nPart2')
json_string = '{"age": 20, "score": 88, "name": "Bob"}'
res2 = json.loads(json_string)
print('res2 = ', res2)


print('\nPart3')

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
def student2dict(std):
    return { 'name': std.name, 'age': std.age, 'score': std.score}

s = Student('Bob', 20, 88)
print(json.dumps(s, default = lambda obj: obj.__dict__))

print('\nPart4')

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

print(json.loads(json_string, object_hook = dict2student))

print('\npart5')
s = json.dumps(json_string, ensure_ascii = False)
print(s)