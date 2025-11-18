num = 0
sum = 0.0
while True:
    value = input("Enter a number: ")

    if value == "done":
        break
    try :
        tot = float(value)
    except:
        print("Ivaalid input")
        continue
    num = num+1
    sum = sum + tot
print(num, sum, sum/num)

