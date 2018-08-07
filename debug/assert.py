
def foo(x):
    a = int(x)
    assert a != 0, 'a is zero'
    return 10/a

def main():
    return foo('0')

main()
