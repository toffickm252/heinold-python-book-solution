
for i in range(15):
    for j in range(15):
        if(i == 0 or i == 15 - 1 or j == 0 or j == 15 - 1):
            print("*", end = " ")
        else:
            print(" ", end=" ")
    print()