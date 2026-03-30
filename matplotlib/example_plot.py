import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
plt.plot(x, y, marker='o')
plt.title('Simple line plot')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()  # uncomment when running interactively
