A = [1,'1','3',4,5,6,'10', 10, 100]
B = [] # int list 
C = [] # string to float list

for i in range(len(A)):
    if(''' type of A[i] is int '''): #if type(A[i] is string)
        B.append(A[i])
    else:
        C.append(A[i])



# part 2 of the coding challenge 

A = input("Input 1 : ")
B = input("Input 2 : ")
Math_in = input("Math type ") # arithmatic of A and B

if('m' in Math_in):
    print(float(A)*float(B))
elif('condition'): # this would be equivilent to elseif in C or another lang
    nothing = 0

C = 0# make c the sum of A + B as a float 