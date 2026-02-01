name = input("Enter student name : ")
maths = int(input("Maths marks : "))
science = int(input("Science marks : "))
english = int(input("English marks : "))

if (maths < 0 or maths > 100) or (science < 0 or science > 100) or (english < 0 or english > 100):
    print("Invalid marks entered")
else:
    total_marks = maths + science + english
    avg_marks = total_marks / 3

    if maths < 40 or science < 40 or english < 40:
        status = "FAIL"
    else:
        status = "PASS"

        if avg_marks >= 75:
            grade = "A"
        elif avg_marks >= 60 and avg_marks < 75:
            grade = "B"
        elif avg_marks >= 40 and avg_marks < 60:
            grade = "C"

print("Student name : ", name)
print("Total Marks : ", total_marks)
print("Percentage : ", round(avg_marks, 2))
print("Status : ", status)

if status == "PASS":
    print("Grade : ", grade)


        
    