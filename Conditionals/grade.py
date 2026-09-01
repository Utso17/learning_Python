def get_name():
    name = input("Please enter a name: ")
    return name

def get_score():
    score = int(input("Please enter the score: "))
    return score

def get_grade():
    score = get_score()

    if score > 100:
        return("score cannot be over then 100")
    elif score >= 90:
        return("A")
    elif score >= 80:
            return("B")
    elif score >= 70:
            return("C")
    elif score >= 60:
            return("D")
    elif score >= 0:
            return("F")
    else:
        return("Score cannot be less then 0")

def main():
    user_name = get_name()
    user_grade = get_grade()

    return user_name, user_grade

student_name , student_grade = main()

print(f"\nStudent Name: {student_name}")
print(f"Letter Grade: {student_grade}")