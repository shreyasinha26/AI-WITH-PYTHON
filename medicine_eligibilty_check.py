# program ask the age of patient, age ia at least 15 and weight is at least 55 kg.
# if age ia atl least 15 but less than 18 years, program also ask the weight.

age = int(input("Enter patient's age: "))

if age < 15:
    print("Not eligible age must be at least 15.")
elif 15 <= age < 18:
    weight = float(input("Enter patient's weight in kg: "))
    if weight >= 55:
        print("Eligible.")
    else:
        print("Not eligible,Weight must be 55 kg.")
else:
    print("Eligible...weight not required.")
