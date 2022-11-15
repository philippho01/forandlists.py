param1 = input("Geben Sie eine Zahl ein: ")
param1 = int(param1)


def quadrat(par1):
    erg = par1*par1
    return erg


for i in range(param1):
    print(i, quadrat(i))