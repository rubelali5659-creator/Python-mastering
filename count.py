count = 0
sum = 0
print("before", count, sum)
for value in [45,55,65,75,85]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print("Result:", count, sum, sum/count)