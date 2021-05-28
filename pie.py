from matplotlib import pyplot as plt
x=[1,2,3,4]
y=[10,2,14,8]
plt.pie(y,labels=x)
plt.title('piechart')
plt.legend()
plt.show()