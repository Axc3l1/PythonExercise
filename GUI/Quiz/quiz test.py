from tkinter import*
import random

names_list = []
global questions_answers
asked = [3,1,4]

questions_answers = {
    1: ["What must you do when you see blue and red flashing lights behind you?",
        'Speed up to get out of the way',
        'Slow down and drive carefully',
        'Slow down and stop',
        'Drive on as usual',
        'Slow down and stop'
        ,3],
    2: ["You may stop on a motorway only:",
        'if there is an emergency', 
        'to let down or pick up passengers', 
        'to make a U-turn', 
        'to stop and take a photo', 
        'if there is an emergency'
        ,1],

    3: ["what is 5+3?",
        '3',
        '2',
        '9',
        '8',
        '8'
        ,4],

}

def randmomiser():
    global qnum
    qnum = random.randint(1,3)
    if qnum not in asked:
        asked.append(qnum)
    elif qnum in asked:
        randmomiser()

class Quizstarter:
    def __init__(self, parent):
        background_color="Oldlace"
        
        self.quiz_frame = Frame(parent, bg = background_color, padx=100, pady=100)
        self.quiz_frame.grid()

        self.heading_label = Label (self.quiz_frame, text = "NZ road rules", font=("Tw Cen MT", "18", "bold"), bg=background_color)
        self.heading_label.grid(row=0)

        self.user_label = Label ( self.quiz_frame, text="Please enter your name below", font=("Tw Cen MT", "16"), bg=background_color)
        self.user_label.grid(row=1, pady=20)

        self.entry_box=Entry(self.quiz_frame)
        self.entry_box.grid(row=2, pady=20)

        self.continue_button = Button (self.quiz_frame, text ="Continue", bg="pink", command=self.name_collection)
        self.continue_button.grid(row=3, pady=20)

    def name_collection(self):
        name = self.entry_box.get()
        names_list.append(name)
        print(names_list)
        self.quiz_frame.destroy()

class Quiz:
    def __init__(self, parent):
        background_color="Oldlace"
        
        self.quiz_frame = Frame(parent, bg = background_color, padx=100, pady=100)
        self.quiz_frame.grid()

        self.question_label = Label (self.quiz_frame, text = questions_answers[qnum][0], font=("Tw Cen MT", "18", "bold"), bg=background_color)
        self.question_label.grid(row=0)

        self.var1=IntVar()

        randmomiser()

        self.rb1 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][1], font=("Helvetica", "12"), bg=background_color)
randmomiser()
if __name__ == "__main__":
    root = Tk()
    root.title("NZ road rules quiz")
    quizstarter_object = Quizstarter(root)
    root.mainloop()

