A = [1,'1','3',4,5,6,'10', 10, 100]
B = []
C = []

for i in range(len(A)):
    if(type(A[i]) is int):
        B.append(A[i])
    else:
        C.append(float(A[i]))

print(C)
print(B)