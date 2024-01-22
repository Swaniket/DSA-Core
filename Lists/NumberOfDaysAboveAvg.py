# Find number of days above average temperature
# 1. It will ask how many day's temp it should consider
# 2. Input those temp
# 3. In Output it will show the avg temp, and how many days have the temp above avg.

numDays = int(input("How many day's temperature?"))
total = 0
above = 0
temp = []

for i in range(1, numDays + 1):
    nextDay = int(input("Day " + str(i) + "'s high temp:"))
    temp.append(nextDay)
    total += nextDay

avg = round(total/numDays, 2)
print("\nAverage = ", str(avg))

for i in temp:
    if i > avg:
        above += 1

print(str(above) + "day(s) above average")
