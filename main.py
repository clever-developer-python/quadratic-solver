import math

a = int(1)
b = int(5)
c = int(6)

pt1 = b*b - 4*a*c

pt2 = (-b - math.sqrt(pt1)) / (2*a)
pt3 = (-b + math.sqrt(pt1))/ (2*a)

print(f'{pt3} or {pt2}')

#credits to this fabulous website, for a kind solution which i implemented, when i was stuck. 
#https://www.programiz.com/python-programming/examples/quadratic-roots
