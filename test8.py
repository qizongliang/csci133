from tkinter import *
from tkinter import ttk
import readquiz
# Load questions from the file animals.txt using the moduel readquiz.py
# you will need atleast three global variables: the list of questions, the
# number of times the player answered, and how many times they were correct:
global questions
global total
global correct


questions = readquiz.loadQuestions()
total = 0
correct = 0

#print(questions)
# creating Tk window
master = Tk()

# creating a Frame which can expand according
# to the size of the window
questionFrame = Frame(master)
questionFrame.pack(fill = BOTH, expand = True)
 
# Display Label
dLab = Label(questionFrame, text="Question:")
dLab.place(relx=0.5, rely=0.5, anchor=CENTER)
dLab.pack(fill = BOTH, expand = True)

question = StringVar()
question.set(questions[total][0])

# QuestionLabel
questionLabel  = Label(questionFrame, textvariable = question)
questionLabel.place(relx=0.5, rely=0.5, anchor=CENTER)
questionLabel.pack(fill = BOTH, expand = True)

# creating a Frame which can expand according
# to the size of the window
buttonFrame = Frame(master)
buttonFrame.pack(fill = BOTH, expand = True)

def trueButtonClick():
    global total
    global correct
    
    if(questions[total][1] == True):
        correct+=1
        score.set("Score:"+str(correct)+"/"+str(total+1))
        feedback.set("Your Answer Was Correct")
        feedbackLabel.config(background = "green")
    else:
        score.set("Score:"+str(correct)+"/"+str(total+1))
        feedback.set("Your Answer Was Incorrect",)
        feedbackLabel.config(background = "pink")
    
    total+=1
    question.set(questions[total][0])

def falseButtonClick():
    global total
    global correct
    
    if(questions[total][1] == False):
        correct+=1
        score.set("Score:"+str(correct)+"/"+str(total+1))
        feedback.set("Your Answer Was Correct")
        feedbackLabel.config(background = "green")
    else:
        score.set("Score:"+str(correct)+"/"+str(total+1))
        feedback.set("Your Answer Was Incorrect")
        feedbackLabel.config(background = "pink")
    
    total+=1
    question.set(questions[total][0],)


# Button True
btnTrue = Button(buttonFrame, text = "True", 
            background = "red", fg = "white",command=trueButtonClick)
btnTrue.pack(side = LEFT, expand = True, fill = BOTH)


# Button False
btnFalse = Button(buttonFrame, text = "False",
            background = "green", fg = "white",command=falseButtonClick)
btnFalse.pack(side = LEFT, expand = True, fill = BOTH)

buttonFrame = Frame(master)

# creating a Frame which can expand according
# to the size of the window
scoreFrame = Frame(master)
scoreFrame.pack(fill = BOTH, expand = True)

score = StringVar()
score.set("Score:"+str(correct)+"/"+str(total))

feedback = StringVar()
feedback.set("Status")
# Button True
feedbackLabel = Label(scoreFrame, textvariable = feedback)
feedbackLabel.pack(side = LEFT, expand = True, fill = BOTH)


# Button False
scoreLabel = Label(scoreFrame,  textvariable = score)
scoreLabel.pack(side = LEFT, expand = True, fill = BOTH)

scoreFrame = Frame(master)


# Execute Tkinter
master.mainloop()



# create a Tkinter interface, arranging widgets as close as possible to the following layout
# (you may use additonal Frame widgets to help arrange buttons and labels):
