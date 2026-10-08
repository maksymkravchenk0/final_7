INPUT_FILE = "students.csv"
OUTPUT_FILE = "result.txt"

math_sum = 0
python_sum = 0
english_sum = 0
number_of_students = 0
best_student = ""
best_student_grade = 0
average = 0

with open(INPUT_FILE) as f:
    next(f)
    for line in f:
        line.strip()
        line = line.split(",")
        line[1] = int(line[1])
        line[2] = int(line[2])
        line[3] = int(line[3])

        math_sum += line[1]
        python_sum += line[2]
        english_sum += line[3]
        number_of_students += 1

        average = (line[1] + line[2] + line[3]) / 3

        if average > best_student_grade:
            best_student_grade = average
            best_student = line[0]

math_average = math_sum / number_of_students
python_average = python_sum / number_of_students
english_average = english_sum / number_of_students

with open(OUTPUT_FILE, "w") as t:
    t.write("Середній бал по класу:\n")
    t.write(f"math: {round(math_average, 2)}\n")
    t.write(f"python: {round(python_average, 2)}\n")
    t.write(f"english: {round(english_average, 2)}\n")
    t.write(f"\nНайкращий студент: {best_student} ({round(best_student_grade, 2)})")

print("Середній бал по класу:\n")
print(f"math: {round(math_average, 2)}\n")
print(f"python: {round(python_average, 2)}\n")
print(f"english: {round(english_average, 2)}\n")
print(f"\nНайкращий студент: {best_student} ({round(best_student_grade, 2)})")



