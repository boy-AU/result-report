import os

os.makedirs("result reports", exist_ok=True)

def grade(score):
    if score >= 70: return "A", 5
    if score >= 60: return "B", 4
    if score >= 50: return "C", 3
    if score >= 45: return "D", 2
    if score >= 40: return "E", 1
    return "F", 0

students = int(input("Number of students: "))

for _ in range(students):
    name = input("\nStudent name: ")
    mat = input("Matric number: ")
    courses = int(input("Number of courses: "))

    total_credit = total_point = 0
    records = []

    for sn in range(1, courses + 1):   # ← SERIAL NUMBER HERE
        print(f"\nCourse {sn}")
        course = input("Course name: ")
        credit = int(input("Credit: "))
        score = int(input("Score: "))

        g, p = grade(score)
        total_credit += credit
        total_point += credit * p

        records.append(f"{sn}\t{course}\t{credit}\t{score}\t{g}")

    gpa = total_point / total_credit

    with open(f"result reports/{name}.txt", "w") as f:
        f.write(f"Student Name: {name}\n")
        f.write(f"Matric Number: {mat}\n\n")
        f.write("SN\tCourse\tCredit\tScore\tGrade\n")
        f.write("\n".join(records))
        f.write(f"\n\nGPA: {gpa:.2f}")

    print("Result saved for", name)

print("\nAll student results saved successfully.")
