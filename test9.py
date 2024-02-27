from tkinter import *
from tkinter import ttk
import tkinter as tk
import random

faceValues = ['ace', '2', '3', '4', '5', '6',
              '7', '8', '9', '10', 'jack',
              'queen', 'king']
suits = ['clubs', 'diamonds', 'hearts',
         'spades']


score = 0
def shuffledDeck():
    deck = []
    for faceValue in faceValues:
        for suit in suits:
            deck.append(faceValue + ' of ' + suit)
    random.shuffle(deck)
    return deck

def faceValueOf(card):
    return card.split()[0]

def suitOf(card):
    return card.split()[2]

def deal(numOfCards):
    return shuffledDeck()[0:numOfCards:1]

def evaluate(hand):
    score = 0
    countMultiple = {}
    for card in hand:
        if faceValueOf(card) in countMultiple:
            countMultiple[faceValueOf(card)]+=1
        else:
            countMultiple[faceValueOf(card)]=1

    for value in countMultiple:
        if(countMultiple[value] == 4):
            score += 100
        elif(countMultiple[value] == 3):
            score +=10
        elif(countMultiple[value] == 2):
            score+=1
    return score
def btnDeal():
    cards = deal(int(textField.get(1.0, "end-1c")))
    score = evaluate(cards)
    return cards

class CardsFrame(tk.Frame):
    def __init__(self,master,*args, **kwargs):
        ttk.Frame.__init__(self,master,*args, **kwargs)
        self.master = master
        
        deck = deal(10)
        
        self.customFrame = Frame(self.master)
        self.customFrame.pack( side = BOTTOM )
        
        for x in deck:
            self.text_variable = StringVar()
            self.text_variable.set(x)

            self.card = Label(self.customFrame, textvariable=self.text_variable, width=25,
                         height=2, borderwidth=3, relief="raised")
            self.card.pack(side = BOTTOM)

    def create_widget(self,cards):
        
        self.customFrame = Frame(self.master)
        self.customFrame.pack( side = BOTTOM )
        for x in cards:
            self.text_variable = StringVar()
            self.text_variable.set(x)

            self.card = Label(self.customFrame, textvariable=self.text_variable, width=25,
                         height=2, borderwidth=3, relief="raised")
            self.card.pack(side = BOTTOM)
        
    def delete_widget(self):
        self.customFrame.destroy()


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
        self.custom_widget = CardsFrame(self)
        self.custom_widget.pack()

        controlFrame = Frame(self)
        controlFrame.pack()
        
        label = Label(controlFrame, text = "Number of cards",width = 25)
        label.pack(side = LEFT)

        self.textField = Text(controlFrame,height = 2,width = 25)
        self.textField.pack(side = LEFT)

        btn = Button(controlFrame, text = "Deal",height = 2,width = 25,command = self.dealcard)
        btn.pack(side = LEFT)

        self.scoreFrame = Frame(self)
        self.scoreFrame.pack()

        self.score_text_variable = StringVar()
        self.score_text_variable.set("Score:"+str(score))

        self.scorelabel=Label(self.scoreFrame, textvariable=self.score_text_variable)
        self.scorelabel.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.scorelabel.pack(side = BOTTOM)
    
    
    def dealcard(self):
        # Call the delete_widget method of the custom widget
        self.custom_widget.delete_widget()
        
        cards = deal(int(self.textField.get(1.0, "end-1c")))
        
        self.score_text_variable.set("Score:"+ str(evaluate(cards)))

        self.scorelabel.destroy()

        self.scorelabel=Label(self.scoreFrame, textvariable=self.score_text_variable)
        self.scorelabel.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.scorelabel.pack(side = BOTTOM)
        
        self.custom_widget.create_widget(cards)

if __name__ == "__main__":
    
    app = App()
    app.mainloop()

