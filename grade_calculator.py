def average(marks):
    return sum(marks) / len(marks)


def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


def is_pass(marks):
    return all(mark >= 35 for mark in marks)


def feedback(avg):
    if avg >= 90:
        return "Excellent performance!"
    elif avg >= 75:
        return "Very good! Keep it up!"
    elif avg >= 50:
        return "Good effort!"
    else:
        return "Keep practicing!"


def main():
    marks = []

    for i in range(3):
        mark = int(input(f"Enter mark for subject {i+1}: "))
        marks.append(mark)

    avg = average(marks)
    result = grade(avg)
    passed = is_pass(marks)
    message = feedback(avg)

    print("\n--- Student Result ---")
    print("Average:", avg)
    print("Grade:", result)
    print("Result:", "Pass" if passed else "Fail")
    print("Feedback:", message)


if __name__ == "__main__":
    main()