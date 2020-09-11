def cycle(decimal):
    decimal = str(decimal)
    lengthOfSection = 1
    found = False
    shave = 0
    while not found:
        cycles = [decimal[i:i + lengthOfSection] for i in range(shave, len(decimal) - lengthOfSection, lengthOfSection)]
        if len(set(cycles)) == 1 and len(cycles) > 1:
            found = True
        elif lengthOfSection < len(decimal) / 2:
            lengthOfSection += 1
        else:
            return 0
    return lengthOfSection

tenPower = ("1" + "0" * 2000)
longestCycle = [0, 0]
for d in range(2, 1000):
    decimal = str((tenPower/ d))
    cycleLength = cycle(decimal)
    if cycleLength > longestCycle[0]:
        longestCycle = [cycleLength, d]
print(longestCycle)

#done!