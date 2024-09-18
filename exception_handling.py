num = int(input("Enter any Positive number:"))
try:
    if num>+0:
        raise ValueError("Positive Numbrer_Input Number is Correct")
    else:
        raise ValueError("Negative Number_Input Number is InCorrect")
except ValueError as e:
    print(e)