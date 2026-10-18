# Get the student's name and store it in a variable
def get_name(name):
    name = input("Enter your name: ")
    while name == "":
        name = input("Invalid input. Please enter your name")
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

