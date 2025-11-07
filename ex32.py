score_input = input("Enter a score between 0.0 & 1.0: ")
try:
    score = float(score_input)
    if score < 0.0 or score > 1.0:
        print("Error: out of range")
    else:
        if score >= 0.9:
            Grade = "A"
        elif score >= 0.8:
            Grade = "B"
        elif score >= 0.7:
            Grade = "C"
        elif score >= 0.6:
            Grade = "D"
        elif score < 0.6:
            Grade = "F"
    print(Grade)
except ValueError:
    print("Error")