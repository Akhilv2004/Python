import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [1, 2, 3, 4, 5]

plt.plot(x, y1, label='y = x^2')
plt.plot(x, y2, label='y = x')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Plot of Two Lines')
plt.legend()

plt.show()
