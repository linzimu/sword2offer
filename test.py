import re


def mul_2(matched):
    val = int(matched.group('val'))
    return str(val * 2)


s = 'A23G4HFD567'
print(re.sub(r'(?P<val>\d+)', mul_2, s))
