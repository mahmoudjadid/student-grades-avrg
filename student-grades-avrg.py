
# im having issues on VS code , cant push normally

def display_student_summary(names, grades):
    for name , grade in (names, grades):
        print(f"{name}, {grade}")

def get_avg_grade(grades):
    if grades == None:
        print("no grades yet")
    return sum(grades)/len(grades)

def get_heighest_grade(names, grades):
    if grades == None:
        print("no grades yet")
    for i in grades:
        if i == max(grades):
            print("max grade = ",names[i], grades[i])

def count_passed(names, grades):
    count = 0 
    for i in grades :
        if i >= 60:
            count+=1
            print ("number of passes",count) 

def main ():
    students_nmber=int(input("enter number of students : "))
    st_names=[]
    st_grade=[]
    for i in range (students_nmber):
        name = input(str("enter name :"))
        grade = float(input("enter grade :"))
        st_grade.append(grade)
        st_names.append(name)
        

display_student_summary(["omar", "mahmoud"], [1,2])
# get_avg_grade(grades)
# get_heighest_grade(names, grades)
# count_passed(names, grades)
# main ()


