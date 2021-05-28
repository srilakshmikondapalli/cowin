from matplotlib import pyplot as plt

x = ['1.2.3.4', '2.3.4.5', '3.4.5.6', '4.5.6.7', '5.6.7.8']
y = [10, 12, 15, 3, 5]
plt.bar(x, y, color=['skyblue', 'orange', 'green', 'yellow', 'pink'], alpha=0.5, width=0.5)
plt.xlabel('IPAddress')
plt.ylabel('Count')
plt.title('IP Address Statistics')
# add text on the bar plot
for i, j in enumerate(y):
    plt.text(x=i, y=j+0.3, s=str(j))
plt.show()