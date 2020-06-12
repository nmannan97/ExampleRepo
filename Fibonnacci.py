start = 1
output = 0
temp = 1

for i in range(8):
    output = start + temp
    temp = start
    start = output

print(output)

A = [1,2,5,3,7,1,1,8,9,10,100,101,20,50,55,32,4]