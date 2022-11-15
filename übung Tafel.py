import matplotlib.pyplot as plt
import math
lst_1 = list(range(-20,20, 1))
lst_2 = [x*x for x in lst_1]

print(lst_1,lst_2)

plt.plot(lst_1,lst_2)
plt.show()
