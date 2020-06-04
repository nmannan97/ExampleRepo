#make a list of 10 items using a for loop

A = [1,3,4,7,3,9,10,8,6,5,5,2]

B = []

for i in range(len(A)):
    if(A[i] not in B):
        B.append(A[i])

for i in range(len(B)):
    current = B[i]
    for j in range(len(B)):
        if(current > B[j]):
            B.insert(j, B[j])
        else:
            break
print(B) #print [0,1,2,3,4,5,6,7,8,9]