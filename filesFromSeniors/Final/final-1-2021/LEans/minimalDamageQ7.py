# Voraruethai Chancharung 6210109
# Question 7: Minimal damage

airCraft = list(map(int, input().split()))

def damage(x):

    if len(x) <= 3:
        return 0
    else:
        tempsum = []
        tempdam = []
        for i in range(len(x)):
            re = 0
            dam = []

            if i == len(x) - 2: # 23
                dam = x[1:i]
                
            elif i == len(x) - 1: # 50
                dam = x[2:i]
    
            else:
                dam = x[:i] + x[i+3:]

            tempsum.append(sum(dam))
            tempdam.append(dam)

        # find minimum
        print(tempsum)
        xmin = min(tempsum)
        indexmin = tempsum.index(xmin)
        xdam = tempdam[indexmin]

        return xmin + damage(xdam)


print(damage(airCraft))

