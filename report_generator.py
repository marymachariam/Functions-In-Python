name = input("Enter your name: ")
backend = int(input("Enter your backend marks: "))
frontend = int(input("Enter your frontend marks: "))
design = int(input("Enter your design marks: "))

def marks_average(backend,frontend, design):
    average = (backend + frontend + design)/3
    return average

def grades(average):
    grade = ""
    if average >= 80:
        grade = "A"
    elif average <= 79 and average >= 70:
        grade = "B"
    elif average <= 69 and average >= 60:
        grade = "C"
    elif average <= 59 and average >= 50:
        grade = "D"
    elif average < 50:
        grade = "E"         
    return grade
    
def students_report():
   
    average = marks_average(backend, frontend, design)
    grade = grades(average)

    final_report = {
        "name" : name,
        "Backend" : backend,
        "Frontend" : frontend,
        "Design" : design,
        "average" : average,
        "grade" : grade
    }
    return final_report


print(students_report())
