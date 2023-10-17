import sys

a = list(map(lambda x: str(x[:-1]).lower(), sys.stdin.readlines()))
d = (sum(['далек' in j[:5] for i in a for j in i.split()]))

print(d)