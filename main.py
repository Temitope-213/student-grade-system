# Get the student's name and store it in a variable
def get_name(name):
    name = input("Enter your name: ")
    while name == "":
        name = input("Invalid input. Please enter your name: ")
    return(name)

# Get the student's age and store it in a variable
def get_age(age):
    while True:
        try:
            age = int(input("Enter your age: "))
            if age > 0:
                return age
            else:
                print("Age must be greater than zero. Please enter a valid age.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

# Get the student's scores for three subjects and store them in a list
def get_scores():
    scores = []
    for i in range(3):
        while True:
            try:
                score = float(input(f"Enter score for subject {i + 1}: "))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("Score must be between 0 and 100. Please enter a valid score.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    return scores

# Get the average score for the student and store it in a variable
def get_average(scores):
    average = sum(scores) / len(scores)
    return round(average, 2)

# Determine the student's grade based on their average score and store it in a variable
def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

# Display the student's report
def display_report(name, age, scores, average, grade):
    total = sum(scores)
    status = "Pass" if average >= 60 else "Fail"

    print("\n===== STUDENT GRADE REPORT =====")
    print("--------------")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Scores: {scores}")
    print(f"Total Score: {total}")
    print(f"Average Score: {average}")
    print(f"Grade: {grade}")
    print(f"Status: {status}")

def main():
    students = []

    while True:
        name = get_name()
        age = get_age()
        scores = get_scores()
        average = get_average(scores)
        grade = get_grade(average)

        student = {
            "name": name,
            "age": age,
            "scores": scores,
            "average": average,
            "grade": grade
        }
        students.append(student)

        display_report(name, age, scores, average, grade)

        another_student = input("\nDo you want to enter another student's information? (yes/no): ").strip().lower()
        if another_student != 'yes':
            break
if __name__ == "__main__":
    main()