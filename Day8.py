import matplotlib.pyplot as plt 

x = []
y = []
for i in range(5):
    x.append(i)
    y.append(i)
    

Area = 0
for i in range(0, len(x)-1):
    Area += 1*y[i] #delta x * y
    plt.gca().add_patch(plt.Rectangle((x[i],0), 1, y[i], fill = False))

print(Area)
plt.text(0,-0.25, 'area = ' + str(Area), fontsize = 8)
plt.plot(x, y)
plt.show()