def rechnung(x):
    return x*x+x

lst_1 = list(range(0,100))

lst_2 = list(map(rechnung,lst_1))
print(lst_2)