import numpy as np
import matplotlib.pyplot as plt
import math


def f(x):
    return (x-0.5) ** 4 + (x-0.5) ** 2 + 5.25

# r = "4x^3+2x; 12x^2+2; 10+x ** 2"
def q(x):
    return 5+x ** 2


x = np.linspace(-2, 2, 200)
y1 = [f(i) for i in x]
y2 = [q(i) for i in x]
plt.plot(x, y1, label='f(x)=$x^4$+$x^2$+5')
plt.plot(x, y2, label='$\phi(x)=x^2+5$')

# 添加标题、坐标轴名称等信息
plt.title('Function contrast')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()

# 显示图形
plt.show()
