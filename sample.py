from matplotlib import pyplot as plt
x=[1,2,3,4]
y=[10,12,3,5]
plt.bar(x,y,color="green",alpha=0.5,width=0.5)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("bar graph")
for i,j  in enumerate(y,1):
    plt.text(x=i,y=j,s=str(j))
plt.show()