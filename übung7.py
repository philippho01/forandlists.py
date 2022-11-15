import matplotlib.pyplot as plt
import math
lst_x = list(range(0,100))
y = [math.sin(x) for x in lst_x]

print(lst_x,y)
plt.plot(lst_x,y)
plt.show()