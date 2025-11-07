def computepay(hours, rate):
    print("In computepay", hours, rate)

sh = input("Enter hour: ")
sr = input("Enter rate: ")
fh = float(sh)
fr = float(sr)
computepay(fh,fr)
if fh>40:
    reg = 40*fr
    otp = (fh-40)*(fr*1.5)
    xp = reg + otp
else:
    xp = fh*fr
print(f"Pay:{xp:.2f}")