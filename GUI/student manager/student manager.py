from tkinter import*



class Student:

    def __init__(self, name):
        self.name = name
    
    def get_grade(self):
        return self.grade
    
    def set_grade(self, grade):
        self.grade = grade

def show_grade(event):
    current_cursor = students_listbox.curselection()
    current_student = current_cursor[0]
    grade_label.config(text=csc_2[current_student].get_grade())




csc_2 = []

csc_2.append(Student("Harry"))
csc_2[0].set_grade("Achived")

window = Tk()
window.geometry("300x300")

students_listbox = Listbox(window)
students_listbox.pack()

csc_2.append(Student("Spike"))
csc_2[1].set_grade("Achieved")
csc_2.append(Student("James"))
csc_2[2].set_grade("Merit")
csc_2.append(Student("Charles"))
csc_2[3].set_grade("Excellence")

grade_label = Label()
grade_label.pack()

show_grade_btn = Button(text="Show Grade", command=show_grade)
show_grade_btn.pack()

window.mainloop()