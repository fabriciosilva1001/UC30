menu = 1

while menu != 5:
    try:
        menu = int(input("1-Soma, 5-Sair: "))

        if menu == 1:
            n1 = float(input("N1: "))
            n2 = float(input("N2: "))
            print(n1 + n2)
            
    except:
        print("Erro")
