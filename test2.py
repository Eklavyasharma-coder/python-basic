s="python is good language"
print("s" in s)
print("J" not in s)


r="python "
if r is "p":
    print("eklavya")

# Input percentage of marks
percentage = float(input("Enter the percentage of marks: "))

# Determine grade
if percentage > 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
else:
    grade = "E"

# Output the result
print("Grade:", grade)
