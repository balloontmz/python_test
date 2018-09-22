import re


def is_valid_email(addr):
    re_addr = re.compile(r'([a-zA-Z][a-zA-Z0-9\_\.]+)\@[a-zA-Z]+[.com]')
    if re_addr.match(addr):
        return True
    else:
        return False


# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')


def name_of_email(addr):
    re_addr = re.compile(r'([\<a-zA-Z\s\>]*?)(\s*)([a-zA-Z][a-zA-Z0-9\_\.]+)\@[a-zA-Z]+[.com]')
    if is_valid_email(addr):
        return re_addr.match(addr).group(3)
    else:
        return re.split(r'[\<\>]+', re_addr.match(addr).group(1))[1]  # 提取字符串，分组


# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')


def name_of_email2(addr):
    # 应该想到这个正则的
    addr_pattern = re.compile(
        r'(\<?([a-zA-Z]+\.?\s?[a-zA-Z]*)\>?\s?[a-zA-Z]*)@([a-zA-z]+)[\.com|\.org]')  # 想的时候有考虑到用这个方式，当时没考虑贪婪匹配：‘？’
    print(addr_pattern.match(addr).groups())
    return addr_pattern.match(addr).group(2)


# 测试:
assert name_of_email2('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email2('tom@voyager.org') == 'tom'
print('ok')
