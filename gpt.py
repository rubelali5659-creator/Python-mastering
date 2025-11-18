largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        value = int(num)
    except:
        print("Invalid input")
        continue

    if largest is None or value > largest:
        largest = value
    if smallest is None or value < smallest:
        smallest = value

print("Maximum is", largest)
print("Minimum is", smallest)
