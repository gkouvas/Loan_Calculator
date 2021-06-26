# put your python code here
a = int(input())
b = int(input())
c = int(input())

p = (a + b + c) / 2
base = p * (p - a) * (p - b) * (p - c)
s = pow(base, 0.5)
print(s)
