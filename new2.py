sh = input("Enter hour: ")
sr = input("Enter rate: ")
try:
    xh = float(sh)
    xr = float(sr)
except:
    print("Error: put numeric number")
    quit()
xp = xh*xr
print(f"Total Pay:{xp:.2f}")