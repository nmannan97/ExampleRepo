import math

A=input("input 1")
B=input("input 2")

math_op=input("input 3")

if('+' in math_op):
    print(float(A)+float(B))
elif('-' in math_op):
    print(float(A)-float(B))
elif('*' in math_op):
    print(float(A)*float(B))
elif('/' in math_op):
    print(float(A)/float(B))
