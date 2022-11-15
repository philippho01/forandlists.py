param_a = int(input("Geben Sie eine Zahl für a ein: "))
param_b = int(input("Geben Sie eine Zahl für b ein: "))

lst_1 = list(range(-20,20))

lst_2 = [param_a * x + param_b for x in lst_1]
print(lst_1)
print(lst_2)