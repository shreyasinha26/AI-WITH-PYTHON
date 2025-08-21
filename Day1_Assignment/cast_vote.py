#if age>18-- true and citizenship true-- right to cast a vote,
# if age<18 and citizenship true-- count years to vote,
#if age >18 and citizenship --false -- no rights to vote
# Voting eligibility check

age = int(input("Enter your age: "))
citizen = input("Enter your citizenship: ")

if age >= 18 and citizen == "indian":
    print("You can cast the vote")
elif age < 18 and citizen == "indian":
    years_left = 18 - age
    print(f"You are eligible to vote {years_left} years.")
elif age >= 18 and citizen != "indian":
    print("You cannot cast the vote because you are not an Indian citizen.")
else:
    print("You can not cast the vote")


