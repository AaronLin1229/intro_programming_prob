def grade_to_letter(grade):
    if grade >= 90: return "A+"
    elif grade >= 85: return "A"
    elif grade >= 80: return "A-"
    elif grade >= 77: return "B+"
    elif grade >= 73: return "B"
    elif grade >= 70: return "B-"
    elif grade >= 67: return "C+"
    elif grade >= 63: return "C"
    elif grade >= 60: return "C-"
    else: return "F"

grade = int(input())
print(grade_to_letter(grade))
