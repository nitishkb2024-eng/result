def calculate_result(mark1, mark2, mark3):
    total = mark1 + mark2 + mark3
    average = total / 3

    if mark1 >= 40 and mark2 >= 40 and mark3 >= 40:
        result = "PASS"
    else:
        result = "FAIL"

    print("Subject 1:", mark1)
    print("Subject 2:", mark2)
    print("Subject 3:", mark3)
    print("Total:", total)
    print("Average:", average)
    print("Result:", result)
# Student marks
mark1 = 75
mark2 = 65
mark3 = 80

calculate_result(mark1, mark2, mark3)