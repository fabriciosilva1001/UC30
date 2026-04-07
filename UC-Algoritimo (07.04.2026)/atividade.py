p = int(input())
d = int(input())
b = int(input())

total = p + (d * 2) + (b * 3)

if total < 100:
    print("N")
else:
    if total < 120:
        print("P")
    else:
        if total < 150:
            print("D")
        else:
            print("B")