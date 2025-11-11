small = None
print()
for value in [9,12,15,18,21,3]:
    if small is None:
        small = value
    
    elif value < small:
        small = value
   
print("Result:", small)